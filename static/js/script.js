ddocument.addEventListener("DOMContentLoaded", function () {
    let alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        alert.addEventListener("closed.bs.alert", function () {
            document.querySelector("main").style.marginTop = "0";
        });
    });

    // Checks if user click outside the navbar when menu is open and closes menu if so
    var navbarToggler = document.querySelector(".navbar-toggler");
    var navbarCollapse = document.querySelector(".navbar-collapse");

    if (!navbarCollapse.contains(event.target) && !navbarToggler.contains(event.target) && navbarCollapse.classList.contains("show")) {
        bootstrap.Collapse.getInstance(navbarCollapse).hide();
    }
});