document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const navList = document.getElementById("nav-list");
  
    menuToggle.addEventListener("click", function () {
      navList.classList.toggle("show");
    });
  
    // Fechar o menu ao clicar em um link
    const navLinks = document.querySelectorAll("#nav-list a");
    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        navList.classList.remove("show");
      });
    });
  });
  