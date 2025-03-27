document.addEventListener("DOMContentLoaded", function () {
  /**
   * Removes the message container if it exists and contains no alerts.
   */
  function removeMessageContainerIfEmpty() {
      const container = document.getElementById("message-container");
      const remainingAlerts = document.querySelectorAll("#message-container .alert");
      if (container && remainingAlerts.length === 0) {
          container.remove();
      }
  }

  /**
   * Handle Bootstrap alert dismissals properly.
   * Removes alert elements and cleans up the container.
   */
  const closeButtons = document.querySelectorAll(".alert .btn-close, .alert .close");
  if (closeButtons.length > 0) {
      closeButtons.forEach(function (button) {
          button.addEventListener("click", function (event) {
              const alertDiv = event.target.closest(".alert");
              if (alertDiv) {
                  alertDiv.remove();
              }
              removeMessageContainerIfEmpty();
          });
      });
  }

  /**
   * Auto-hide messages after 5 seconds and clean up the container.
   */
  setTimeout(function () {
      const alerts = document.querySelectorAll("#message-container .alert");
      if (alerts.length > 0) {
          alerts.forEach(function (alertDiv) {
              alertDiv.remove();
          });
          removeMessageContainerIfEmpty();
      }
  }, 5000);

  /**
   * Close navbar if clicking outside of the toggler and menu.
   */
  document.addEventListener("click", function (event) {
      const navbarToggler = document.querySelector(".navbar-toggler");
      const navbarCollapse = document.querySelector(".navbar-collapse");

      if (navbarCollapse && navbarToggler) {
          const isClickOutside =
              !navbarCollapse.contains(event.target) &&
              !navbarToggler.contains(event.target) &&
              navbarCollapse.classList.contains("show");

          if (isClickOutside) {
              const instance = bootstrap.Collapse.getInstance(navbarCollapse);
              if (instance) {
                  instance.hide();
              }
          }
      }
  });
});
