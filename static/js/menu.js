document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    const menuBtn = document.querySelector('.menu-btn');
    const mainContent = document.querySelector('.main-content');

    menuBtn.addEventListener('click', function() {
        if (sidebar.style.transform === 'translateX(0px)') {
            sidebar.style.transform = 'translateX(-100%)';
            mainContent.style.marginLeft = '0px';
        } else {
            sidebar.style.transform = 'translateX(0px)';
            mainContent.style.marginLeft = '270px';
        }
    });
});
