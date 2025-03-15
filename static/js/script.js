document.addEventListener("DOMContentLoaded", function () {
  // Handle Bootstrap alert dismissals properly
  let alerts = document.querySelectorAll(".alert");

  // Close navbar when clicking outside of it
  document.addEventListener("click", function (event) {
    var navbarToggler = document.querySelector(".navbar-toggler");
    var navbarCollapse = document.querySelector(".navbar-collapse");

    if (navbarCollapse && navbarToggler) {
      if (
        !navbarCollapse.contains(event.target) &&
        !navbarToggler.contains(event.target) &&
        navbarCollapse.classList.contains("show")
      ) {
        bootstrap.Collapse.getInstance(navbarCollapse).hide();
      }
    }
  });
});
