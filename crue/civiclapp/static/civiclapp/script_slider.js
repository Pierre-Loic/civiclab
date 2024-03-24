document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector('.slider');
    const beforeImage = document.querySelector('.after-image');
    let isDragging = false;

    const updateImagePosition = (x) => {
        const { left, width } = slider.parentElement.getBoundingClientRect();
        x = x - left;
        if (x < 0) x = 0;
        else if (x > width) x = width;
        
        const percentage = (x / width) * 100;
        slider.style.left = `${percentage}%`;
        beforeImage.style.clipPath = `polygon(${percentage}% 0, 100% 0, 100% 100%, ${percentage}% 100%)`;
    };

    // Gestion des événements pour les souris
    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        updateImagePosition(e.clientX);
    });

    slider.addEventListener('mousedown', () => {
        isDragging = true;
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });

    // Gestion des événements pour les touches tactiles
    document.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        const touch = e.touches[0];
        updateImagePosition(touch.clientX);
        e.preventDefault(); // Empêcher le comportement de défilement par défaut sur les appareils tactiles
    }, { passive: false });

    slider.addEventListener('touchstart', (e) => {
        isDragging = true;
        e.preventDefault(); // Empêcher le comportement de défilement par défaut sur les appareils tactiles lors du démarrage de l'interaction
    }, { passive: false });

    document.addEventListener('touchend', () => {
        isDragging = false;
    });
});


