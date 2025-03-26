document.addEventListener("DOMContentLoaded", function () {
    // Handle Bootstrap alert dismissals properly
    document.querySelectorAll(".alert .close").forEach(function(button) {
      button.addEventListener("click", function(event) {
          // Find the parent alert div and remove it
          let alertDiv = event.target.closest(".alert");
          if (alertDiv) {
              alertDiv.remove();
          }

          // Check if there are any messages left
          if (document.querySelectorAll("#message-container .alert").length === 0) {
              let container = document.getElementById("message-container");
              if (container) {
                  container.remove();
              }
          }
      });
  });

  // Auto-hide messages after 5 seconds
  setTimeout(function() {
      document.querySelectorAll(".alert").forEach(function(alertDiv) {
          alertDiv.remove();
      });

      let container = document.getElementById("message-container");
      if (container && document.querySelectorAll("#message-container .alert").length === 0) {
          container.remove();
      }
  }, 5000);


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
