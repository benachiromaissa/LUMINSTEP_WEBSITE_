const menuOpenButton = document.getElementById('menu-open-button');
const menuCloseButton = document.getElementById('menu-close-button');
const navMenu = document.querySelector('.navbar .nav-menu');

menuOpenButton.addEventListener('click', () => {
    navMenu.style.display = 'flex';
    menuOpenButton.style.display = 'none';
    menuCloseButton.style.display = 'block';
});

menuCloseButton.addEventListener('click', () => {
    navMenu.style.display = 'none';
    menuOpenButton.style.display = 'block';
    menuCloseButton.style.display = 'none';
});




const container = document.getElementById("container");
        const overlayCon = document.getElementById("overlayCon");
        const overlayBtn = document.getElementById("overlayBtn");
    
        overlayBtn.addEventListener('click', () => {
            container.classList.toggle('right-panel-active');

            overlayBtn.classList.remove('btnScaled');
            window.requestAnimationFrame(() => {
                overlayBtn.classList.add('btnScaled');
            });
        });