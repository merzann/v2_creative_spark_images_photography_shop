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

  // Validate required billing fields and country-specific postcode format
  function validateBillingFormFields() {
    const form = document.getElementById('billing-form');
    if (!form) return false;

    const requiredFields = [
      'billing_street1',
      'billing_city',
      'billing_postcode',
      'billing_country',
      'billing_phone',
    ];

    for (let id of requiredFields) {
      const input = form.querySelector(`#${id}`);
      if (!input || input.value.trim() === '') return false;
    }

    const country = form.querySelector('#billing_country')?.value;
    const postcode = form.querySelector('#billing_postcode')?.value.trim();

    return validatePostalCode(postcode, country);
  }

  // Country-specific postal code validation rules
  function validatePostalCode(postcode, country) {
    if (!postcode || !country) return false;

    const rules = {
      IE: /^[A-Z]{1}[0-9]{2}\s?[A-Z0-9]{4}$/i,    // Ireland (e.g. D04, T12ABC1)
      DE: /^\d{5}$/,                              // Germany (e.g. 10115)
      AT: /^\d{4}$/,                              // Austria (e.g. 1010)
      US: /^\d{5}(-\d{4})?$/,                     // USA (e.g. 12345 or 12345-6789)
      GB: /^[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2}$/i // UK (e.g. SW1A 1AA)
    };

    const regex = rules[country] || /^[A-Z0-9\s\-]{3,10}$/; // Default fallback
    return regex.test(postcode);
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
    const form = document.querySelector('form');
    if (!form) return;
    formInitialData = {};
    new FormData(form).forEach((value, key) => {
      formInitialData[key] = value;
    });
  }

  // Revert form values back to the original state
  function resetFormToInitialValues() {
    const form = document.querySelector('form');
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
    const form = document.querySelector('form');
    if (!form) return false;
    const currentData = {};
    new FormData(form).forEach((value, key) => {
      currentData[key] = value;
    });
    return Object.keys(formInitialData).some(
      key => currentData[key] !== formInitialData[key]
    );
  }

  // Load and display billing form (Step 2)
  function loadBillingForm() {
    fetch('/checkout/load-billing-form/')
      .then(response => {
        if (!response.ok) {
          throw new Error("Failed to load billing form");
        }
        return response.text();
      })
      .then(html => {
        formWrapper.innerHTML = html;
        formWrapper.style.display = 'block';

        // Reset redirect flag
        continueBtn.disabled = false;
        continueBtn.dataset.allowRedirect = "false";

        // Capture original values for change tracking
        captureInitialFormValues();

        // Set up modal logic for billing changes
        ['billing_street1', 'billing_postcode', 'billing_city', 'billing_country'].forEach(id => {
          const input = document.getElementById(id);
          if (input) {
            input.addEventListener('input', () => {
              // Disable Continue unless billing form is valid
              const isValid = validateBillingFormFields();
              continueBtn.disabled = !isValid;

              continueBtn.dataset.allowRedirect = "false";
              skipProfileSave = false;
            });
          }
        });

        // Trigger validation after rendering
        continueBtn.disabled = !validateBillingFormFields();

        // Replace Continue button click logic for billing step
        continueBtn.onclick = function () {
          if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave) {
            window.location.href = '/checkout/summary/';
            return;
          }

          if (formHasChanges()) {
            continueBtn.disabled = true;
            modalAlert.classList.add('d-none');
            saveModal.show();
          } else {
            window.location.href = '/checkout/summary/';
          }
        };
      })
      .catch(error => {
        console.error("Billing form load failed:", error);
      });
  }

  // Handle "Save" button in the modal
  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'save-profile') {
      const form = document.querySelector('form');
      const formData = new FormData(form);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

      const email = form.querySelector('input[name="email"]')?.value.trim();
      const url = form.id === 'billing-form'
        ? '/checkout/save-billing-from-checkout/'
        : '/checkout/save-profile-from-checkout/';

      // Basic email validation for profile form
      if (form.id === 'checkout-profile-form' && !isValidEmail(email)) {
        modalAlert.classList.remove('d-none');
        modalAlert.textContent = "Please enter a valid email address.";
        return;
      }

      // Submit form data via AJAX
      fetch(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrfToken },
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

            // Refresh saved values
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
    if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave === true) {
      // Proceed to billing if profile is saved or skipped
      loadBillingForm();
      return;
    }

    // Prompt save modal if form has been edited
    if (formHasChanges()) {
      continueBtn.disabled = true;
      modalAlert.classList.add('d-none');
      saveModal.show();
    } else {
      loadBillingForm();
    }
  });

  // Auto-fill form for logged-in users
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
              aria-label="First Name" value="${document.body.dataset.firstName || ''}" required>
          </div>

          <div class="mb-3">
            <label for="last_name" class="form-label">Last Name</label>
            <input type="text" class="form-control" name="last_name" id="last_name"
              aria-label="Last Name" value="${document.body.dataset.lastName || ''}" required>
          </div>

          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" name="email" id="email"
              aria-label="Email address" value="${document.body.dataset.email || ''}" required>
          </div>
        </form>
      </div>
    `;

    formWrapper.style.display = 'block';
    continueBtn.disabled = false;
    captureInitialFormValues();

    // Track changes in form
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

  // Handle login and guest actions
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');

  if (loginBtn) {
    loginBtn.addEventListener('click', function () {
      // Redirect to login with next to checkout
      window.location.href = '/accounts/login/?next=/checkout/';
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      // Fetch and show guest profile form
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

          // Enable on valid input
          ['first_name', 'last_name', 'email'].forEach(id => {
            const input = document.getElementById(id);
            if (input) {
              input.addEventListener('input', () => {
                continueBtn.disabled = !validateGuestFormFields();
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
