const socket = io.connect('http://' + document.domain + ':' + location.port + '/status');
    socket.on('update_status', function(data) {
        const patientElement = document.getElementById('patient_' + data.id);
        if (patientElement) {
            const statusElement = patientElement.querySelector('.status');
            if (data.status === 'online') {
                statusElement.classList.remove('offline');
                statusElement.classList.add('online');
            } else {
                statusElement.classList.remove('online');
                statusElement.classList.add('offline');
            }
        }
    });