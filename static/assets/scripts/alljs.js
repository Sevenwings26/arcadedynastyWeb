const button = document.querySelector('#menu-button');
const menu = document.querySelector('#menu');


button.addEventListener('click', () => {
  menu.classList.toggle('hidden');
});


// Initialize the carousel
document.addEventListener('DOMContentLoaded', function () {
  // Initialize Bootstrap carousel
  const carouselElement = document.querySelector('#carouselExampleControls');
  const carousel = new bootstrap.Carousel(carouselElement, {
    interval: false,
    pause: 'hover'
  });

  // Add event listeners for previous and next controls
  document.querySelector('.carousel-control-prev').addEventListener('click', function () {
    carousel.prev();  // Move to the previous slide
  });

  document.querySelector('.carousel-control-next').addEventListener('click', function () {
    carousel.next();  // Move to the next slide
  });
});
