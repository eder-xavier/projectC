document.addEventListener('DOMContentLoaded', function () {
  const sliders = document.querySelectorAll('.slider');

  sliders.forEach((slider) => {
    const slidesContainer = slider.querySelector('.slides');
    const slides = slider.querySelectorAll('.slide');
    const dots = slider.querySelectorAll('.dot');
    let currentSlide = 0;
    let intervalId;

    function showSlide(index) {
      slidesContainer.style.transform = `translateX(${-100 * index}%)`;

      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
      });
    }

    function nextSlide() {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }

    function prevSlide() {
      currentSlide = (currentSlide - 1 + slides.length) % slides.length;
      showSlide(currentSlide);
    }

    function onDotClick(index) {
      currentSlide = index;
      showSlide(currentSlide);
    }

    function startAutoSlide() {
      intervalId = setInterval(() => {
        nextSlide();
      }, 9000); // 5000 milliseconds = 5 seconds 
    }

    function stopAutoSlide() {
      clearInterval(intervalId);
    }

    slider.addEventListener('mouseenter', stopAutoSlide);
    slider.addEventListener('mouseleave', startAutoSlide);

    slider.querySelector('.next').addEventListener('click', () => {
      nextSlide();
      stopAutoSlide();
    });

    slider.querySelector('.prev').addEventListener('click', () => {
      prevSlide();
      stopAutoSlide();
    });

    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        onDotClick(index);
        stopAutoSlide();
      });
    });

    // Initial setup
    showSlide(currentSlide);
    startAutoSlide();
  });
});
