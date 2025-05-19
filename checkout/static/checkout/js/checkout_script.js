document.addEventListener('DOMContentLoaded', function () {
  // Grab key DOM elements
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";

  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));

  let formInitialData = {};
  let skipProfileSave = false;

  // Validate email format (simple regex)
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Validate required guest fields and email format
  function validateGuestFormFields() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;

    const firstName = form.querySelector('#first_name')?.value.trim();
    const lastName = form.querySelector('#last_name')?.value.trim();
    const email = form.querySelector('#email')?.value.trim();

    return firstName && lastName && isValidEmail(email);
  }

  // Capture initial form values to detect changes later
  function captureInitialFormValues() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return;
    formInitialData = {};
    new FormData(form).forEach((value, key) => {
      formInitialData[key] = value;
    });
  }

  // Revert form values back to the original state
  function resetFormToInitialValues() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return;
    Object.entries(formInitialData).forEach(([key, value]) => {
      const field = form.querySelector(`[name="${key}"]`);
      if (field) {
        field.value = value;
      }
    });
  }

  // Check if any form values have changed from the initial state
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

  // Handle "Save" button in the modal
  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'save-profile') {
      const form = document.getElementById('checkout-profile-form');
      const formData = new FormData(form);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
      const email = form.querySelector('input[name="email"]')?.value.trim();

      // Basic email format validation
      if (!isValidEmail(email)) {
        modalAlert.classList.remove('d-none');
        modalAlert.textContent = "Please enter a valid email address.";
        return;
      }

      // Submit the profile form via AJAX
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
            // Hide modal and allow redirect
            const modalElement = document.getElementById('saveModal');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();

            continueBtn.dataset.allowRedirect = "true";
            continueBtn.disabled = false;
            modalAlert.classList.add('d-none');

            // Update initial values so further changes are tracked correctly
            captureInitialFormValues();
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

  // Handle "Don't Save" or "Cancel" modal actions
  document.addEventListener('click', function (event) {
    if (
      event.target &&
      (event.target.id === 'skip-save' || event.target.textContent.trim() === 'Cancel')
    ) {
      skipProfileSave = true;
      continueBtn.dataset.allowRedirect = "true";
      continueBtn.disabled = false;

      // Reset form only for authenticated users
      if (isAuthenticated) {
        resetFormToInitialValues();
      }

      const modalElement = document.getElementById('saveModal');
      const modalInstance = bootstrap.Modal.getInstance(modalElement);
      modalInstance.hide();
    }
  });

  // Handle click on "Continue" button
  continueBtn.addEventListener('click', function () {
    // Allow redirect if profile save is skipped or already approved
    if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave === true) {
      window.location.href = '/checkout/billing/';
      return;
    }

    // Prompt save modal if form was changed
    if (formHasChanges()) {
      continueBtn.disabled = true;
      modalAlert.classList.add('d-none');
      saveModal.show();
    } else {
      window.location.href = '/checkout/billing/';
    }
  });

  // Auto-inject form for authenticated users
  if (isAuthenticated) {
    formWrapper.innerHTML = `
      <div class="card p-4 shadow-sm">
        <h5 class="mb-3">Welcome back!</h5>
        <form id="checkout-profile-form">
          <input type="hidden" name="csrfmiddlewaretoken"
            value="${document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''}">

          <div class="mb-3">
            <label for="first_name" class="form-label">First Name</label>
            <input
              type="text"
              class="form-control"
              name="first_name"
              id="first_name"
              aria-label="First Name"
              value="${document.body.dataset.firstName || ''}"
              required
            >
          </div>

          <div class="mb-3">
            <label for="last_name" class="form-label">Last Name</label>
            <input
              type="text"
              class="form-control"
              name="last_name"
              id="last_name"
              aria-label="Last Name"
              value="${document.body.dataset.lastName || ''}"
              required
            >
          </div>

          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input
              type="email"
              class="form-control"
              name="email"
              id="email"
              aria-label="Email address"
              value="${document.body.dataset.email || ''}"
              required
            >
          </div>
        </form>
      </div>
    `;

    formWrapper.style.display = 'block';
    continueBtn.disabled = false;
    captureInitialFormValues();

    // Revoke redirect permission if user changes form again
    ['first_name', 'last_name', 'email'].forEach(id => {
      const input = document.getElementById(id);
      if (input) {
        input.addEventListener('input', () => {
          continueBtn.dataset.allowRedirect = "false";
          skipProfileSave = false;
        });
      }
    });
  }

  // Setup login and guest checkout options
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');

  if (loginBtn) {
    loginBtn.addEventListener('click', function () {
      window.location.href = '/accounts/login/?next=/checkout/';
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      // Load guest form asynchronously
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

          // Disable continue initially
          continueBtn.disabled = !validateGuestFormFields();

          // Enable continue when valid input is detected
          ['first_name', 'last_name', 'email'].forEach(id => {
            const input = document.getElementById(id);
            if (input) {
              input.addEventListener('input', () => {
                continueBtn.disabled = !validateGuestFormFields();

                // Revoke redirect permission if guest changes data again
                continueBtn.dataset.allowRedirect = "false";
                skipProfileSave = false;
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
