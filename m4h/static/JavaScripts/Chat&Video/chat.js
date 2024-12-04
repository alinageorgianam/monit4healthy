document.addEventListener('DOMContentLoaded', function() {
    const currentUserId = document.getElementById('current-user-id').value = "{{ session['id'] }}";

    document.querySelectorAll('.chat-button').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-user-id');
            const userName = this.getAttribute('data-user-name');
            openChat(userId, userName);
        });
    });

    document.querySelectorAll('.video-call-button').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-user-id');
            const userName = this.getAttribute('data-user-name');
            startVideoCall(userId);
        });
    });

    function openChat(userId, userName) {
        document.getElementById('chat-container').style.display = 'block';
        document.getElementById('chat-header').textContent = `Chat with ${userName}`;
        document.getElementById('chat-header').setAttribute('data-user-id', userId);
        fetchMessages(userId);
    }

    function closeChat() {
        document.getElementById('chat-container').style.display = 'none';
    }

    function fetchMessages(userId) {
        fetch(`/get_messages/${userId}`)
            .then(response => response.json())
            .then(data => {
                data.messages = undefined;
                if (data.error) {
                    console.error('Error fetching messages:', data.error);
                } else {
                    const messagesContainer = document.getElementById('chat-messages');
                    messagesContainer.innerHTML = '';
                    data.messages.forEach(message => {
                        message.sender_id = undefined;
                        message.sender_name = undefined;
                        const messageElement = document.createElement('div');
                        messageElement.classList.add('message', message.sender_id === currentUserId ? 'sent' : 'received');
                        messageElement.innerHTML = `<strong>${message.sender_name}</strong><p>${message.message}</p><span class="timestamp">${new Date(message.timestamp).toLocaleString()}</span>`;
                        messagesContainer.appendChild(messageElement);
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    function sendMessage(event) {
        event.preventDefault();
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value;
        const userId = document.getElementById('chat-header').getAttribute('data-user-id');
        messageInput.value = '';

        fetch(`/send_message`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: userId, message: message })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error('Error sending message:', data.error);
            } else {
                fetchMessages(userId);
            }
        })
        .catch(error => console.error('Error:', error));
    }

    document.getElementById('chat-form').addEventListener('submit', sendMessage);
    document.getElementById('close-chat').addEventListener('click', closeChat);

    function startVideoCall() {
        document.getElementById('video-container').style.display = 'flex';
        navigator.mediaDevices.getUserMedia({ video: true, audio: true })
            .then(stream => {
                const localVideo = document.getElementById('local-video');
                localVideo.srcObject = stream;
                // Additional code to set up WebRTC connection would go here
            })
            .catch(error => console.error('Error accessing media devices.', error));
    }

    function endCall() {
        const localVideo = document.getElementById('local-video');
        const remoteVideo = document.getElementById('remote-video');
        if (localVideo.srcObject) {
            localVideo.srcObject.getTracks().forEach(track => track.stop());
        }
        if (remoteVideo.srcObject) {
            remoteVideo.srcObject.getTracks().forEach(track => track.stop());
        }
        document.getElementById('video-container').style.display = 'none';
        // Additional code to close WebRTC connection would go here
    }

    document.getElementById('close-video').addEventListener('click', endCall);
});
