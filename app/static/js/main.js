// Mostrar logo placeholder si no carga la imagen
document.addEventListener('DOMContentLoaded', () => {
    const logoImg = document.querySelector('Gastro_Basque Logo.png');
    const logoPlaceholder = document.querySelector('.logo-placeholder');

    if (logoImg && logoPlaceholder) {
        logoImg.addEventListener('error', () => {
            logoImg.style.display = 'none';
            logoPlaceholder.style.display = 'flex';
        });

        if (!logoImg.src || logoImg.naturalWidth === 0) {
            logoImg.style.display = 'none';
            logoPlaceholder.style.display = 'flex';
        }
    }

    // Resaltar enlace activo en el navbar
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.background = 'rgba(0,0,0,0.1)';
            link.style.color = '#2a2a1f';
        }
    });
});