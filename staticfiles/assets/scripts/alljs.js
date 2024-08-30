// toggle button control
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


// ca
const body = document.body
const slides = document.querySelectorAll('.slide')
const leftBtn = document.getElementById('left')
const rightBtn = document.getElementById('right')

let activeSlide = 0

rightBtn.addEventListener('click', () => {
  activeSlide++

  if (activeSlide > slides.length - 1) {
    activeSlide = 0
  }

  setBgToBody()
  setActiveSlide()
})

leftBtn.addEventListener('click', () => {
  activeSlide--

  if (activeSlide < 0) {
    activeSlide = slides.length - 1
  }

  setBgToBody()
  setActiveSlide()
})

setBgToBody()

function setBgToBody() {
  body.style.backgroundImage = slides[activeSlide].style.backgroundImage
}

function setActiveSlide() {
  slides.forEach((slide) => slide.classList.remove('active'))

  slides[activeSlide].classList.add('active')
}