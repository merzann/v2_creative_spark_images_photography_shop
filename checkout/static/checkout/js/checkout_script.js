document.addEventListener('DOMContentLoaded', function () {
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";

  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));

  let formInitialData = {};
  let skipProfileSave = false;

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

  function validateGuestFormFields() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;

    const firstName = form.querySelector('#first_name')?.value.trim();
    const lastName = form.querySelector('#last_name')?.value.trim();
    const email = form.querySelector('#email')?.value.trim();

    return firstName && lastName && email;
  }

  // Save button inside modal
  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'save-profile') {
      const form = document.getElementById('checkout-profile-form');
      const formData = new FormData(form);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

      fetch('/checkout/save-profile-from-checkout/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
        },
        body: formData,
      })
        .then(response => response.json())
        .then(data => {
          if (data && data.success) {
            const modalElement = document.getElementById('saveModal');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();

            continueBtn.dataset.allowRedirect = "true";
            continueBtn.disabled = false;
            modalAlert.classList.add('d-none');
          } else {
            throw new Error('Unexpected response from server');
          }
        })
        .catch(error => {
          console.error('Error saving profile:', error);
          modalAlert.classList.remove('d-none');
          modalAlert.textContent = "Unable to save your profile. Please try again.";
          continueBtn.disabled = false;
        });
    }
  });

  // Don't Save or Cancel
  document.addEventListener('click', function (event) {
    if (
      event.target &&
      (event.target.id === 'skip-save' || event.target.textContent.trim() === 'Cancel')
    ) {
      skipProfileSave = true;
      continueBtn.dataset.allowRedirect = "true";
      continueBtn.disabled = false;

      const modalElement = document.getElementById('saveModal');
      const modalInstance = bootstrap.Modal.getInstance(modalElement);
      modalInstance.hide();
    }
  });

  // Continue button logic
  continueBtn.addEventListener('click', function () {
    if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave === true) {
      window.location.href = '/checkout/billing/';
      return;
    }

    if (formHasChanges()) {
      continueBtn.disabled = true;
      modalAlert.classList.add('d-none');
      saveModal.show();
    } else {
      window.location.href = '/checkout/billing/';
    }
  });

  // Authenticated user form
  if (isAuthenticated) {
    formWrapper.innerHTML = `
      <div class="card p-4 shadow-sm">
        <h5 class="mb-3">Welcome back!</h5>
        <form id="checkout-profile-form">
          <input type="hidden" name="csrfmiddlewaretoken"
          value="${document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''}">

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
  }

  // Login / Guest buttons
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
          captureInitialFormValues();

          // Disable continue by default
          continueBtn.disabled = !validateGuestFormFields();

          // Enable only when all required fields are filled
          ['first_name', 'last_name', 'email'].forEach(id => {
            const input = document.getElementById(id);
            if (input) {
              input.addEventListener('input', () => {
                continueBtn.disabled = !validateGuestFormFields();
              });
            }
          });
        })
        .catch(error => {
          console.error("Guest form load failed:", error);
        });
    });
  }
});
