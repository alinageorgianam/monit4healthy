document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.clickable-image').forEach(image => {
        image.addEventListener('click', function() {
            showImageModal(this.getAttribute('data-image-src'));
        });
    });

    function showImageModal(imageSrc) {
        var modal = document.getElementById("imageModal");
        var modalImg = document.getElementById("modalImage");
        modal.style.display = "block";
        modalImg.src = imageSrc;
    }

    function closeImageModal() {
        var modal = document.getElementById("imageModal");
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        var modal = document.getElementById("imageModal");
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Expose the functions to the global scope
    window.showImageModal = showImageModal;
    window.closeImageModal = closeImageModal;
});
