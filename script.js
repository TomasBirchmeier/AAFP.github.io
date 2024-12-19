document.getElementById('menu-toggle').addEventListener('click', function() {
    const navMenu = document.getElementById('nav-menu');
    navMenu.classList.toggle('active');
});
// Selecciona los botones y el contenedor de las slides
<script>
    let currentIndex = 0; // Índice de la imagen actual
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    function showSlide(index) {
        slides.style.transform = `translateX(-${index * 100}%)`;
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides; // Mueve al siguiente o vuelve al inicio
        showSlide(currentIndex);
    }

    setInterval(nextSlide, 5000); // Cambiar cada 5 segundos
    showSlide(currentIndex); // Mostrar la primera imagen
</script>