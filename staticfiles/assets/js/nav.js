document.addEventListener('DOMContentLoaded', function () {
    const navbarToggler = document.getElementById('navbar-toggler');
    const navbarHost = document.getElementById('navbars-host');
  
    // Toggle navbar visibility on small screens
    navbarToggler.addEventListener('click', function () {
      if (navbarHost.classList.contains('hidden')) {
        navbarHost.classList.remove('hidden');
        navbarHost.classList.add('block');
      } else {
        navbarHost.classList.add('hidden');
        navbarHost.classList.remove('block');
      }
    });
  
    // Optional: Handle dropdown menu display
    const dropdownToggle = document.getElementById('dropdown-a');
    const dropdownMenu = document.getElementById('dropdown-menu');
  
    dropdownToggle.addEventListener('click', function () {
      dropdownMenu.classList.toggle('hidden');
    });
  
    // Close dropdown menu when clicking outside
    document.addEventListener('click', function (event) {
      if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.add('hidden');
      }
    });
  });
  