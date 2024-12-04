document.addEventListener('DOMContentLoaded', function() {
    const imageItems = document.querySelectorAll('.clickable-image');
    imageItems.forEach(item => {
        item.addEventListener('click', function() {
            showImageModal(this.dataset.imageSrc);
        });
    });
});

function showImageModal(imageSrc) {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");
    modal.style.display = "block";
    modalImg.src = imageSrc;
}

function closeImageModal() {
    const modal = document.getElementById("imageModal");
    modal.style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("imageModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
}
