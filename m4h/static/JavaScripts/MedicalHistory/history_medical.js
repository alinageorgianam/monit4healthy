document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.clickable-image').forEach(image => {
        image.addEventListener('click', function() {
            showImageModal(this.getAttribute('data-image-src'));
        });
    });

    // Expose the functions to the global scope
    window.showImageModal = showImageModal;
    window.closeImageModal = closeImageModal;
});
