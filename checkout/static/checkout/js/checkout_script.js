document.addEventListener('DOMContentLoaded', function () {
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";

  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));

  let formInitialData = {};

  function captureInitialFormValues() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return;
    formInitialData = {};
    new FormData(form).forEach((value, key) => {
      formInitialData[key] = value;
    });
  }

  function formHasChanges() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;
    const currentData = {};
    new FormData(form).forEach((value, key) => {
      currentData[key] = value;
    });
    return Object.keys(formInitialData).some(
      key => currentData[key] !== formInitialData[key]
    );
  }

  // Attach Save button handler globally
  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'save-profile') {
      const form = document.getElementById('checkout-profile-form');
      const formData = new FormData(form);

      fetch('/checkout/save-profile-from-checkout/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          window.location.href = '/checkout/billing/';
        })
        .catch(error => {
          console.error('Error saving profile:', error);
          modalAlert.classList.remove('d-none');
          modalAlert.textContent = "Unable to save your profile. Please try again.";
        });
    }
  });

  // Skip saving and go to billing
  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'skip-save') {
      window.location.href = '/checkout/billing/';
    }
  });

  // Authenticated user
  if (isAuthenticated) {
    formWrapper.innerHTML = `
      <div class="card p-4 shadow-sm">
        <h5 class="mb-3">Welcome back!</h5>
        <form id="checkout-profile-form">
          <div class="mb-3">
            <label for="first_name" class="form-label">First Name</label>
            <input type="text" class="form-control" name="first_name" id="first_name"
              value="${document.body.dataset.firstName || ''}" required>
          </div>
          <div class="mb-3">
            <label for="last_name" class="form-label">Last Name</label>
            <input type="text" class="form-control" name="last_name" id="last_name"
              value="${document.body.dataset.lastName || ''}" required>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" name="email" id="email"
              value="${document.body.dataset.email || ''}" required>
          </div>
        </form>
      </div>
    `;

    formWrapper.style.display = 'block';
    continueBtn.disabled = false;
    captureInitialFormValues();

    continueBtn.addEventListener('click', function () {
      if (formHasChanges()) {
        saveModal.show();
      } else {
        window.location.href = '/checkout/billing/';
      }
    });
  }

  // Guest logic
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');

  if (loginBtn) {
    loginBtn.addEventListener('click', function () {
      window.location.href = '/accounts/login/?next=/checkout/';
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      fetch('/checkout/load-guest-form/')
        .then(response => {
          if (!response.ok) {
            throw new Error("Failed to load guest form");
          }
          return response.text();
        })
        .then(html => {
          formWrapper.innerHTML = html;
          formWrapper.style.display = 'block';
          continueBtn.disabled = false;
          captureInitialFormValues();

          continueBtn.addEventListener('click', function () {
            if (formHasChanges()) {
              saveModal.show();
            } else {
              window.location.href = '/checkout/billing/';
            }
          });
        })
        .catch(error => {
          console.error("Guest form load failed:", error);
        });
    });
  }
});
