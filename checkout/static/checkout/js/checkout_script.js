document.addEventListener('DOMContentLoaded', function () {
  // Grab key DOM elements
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";

  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));

  let formInitialData = {};
  let skipProfileSave = false;

    /**
   * Updates the visual progress tracker to highlight the active step.
   * @param {number} stepNumber - The step to activate (1–5)
   */
  function setActiveProgressStep(stepNumber) {
    const steps = document.querySelectorAll('.progress-steps .step');
    steps.forEach((stepEl, index) => {
      if (index === stepNumber - 1) {
        stepEl.classList.add('step-active');
      } else {
        stepEl.classList.remove('step-active');
      }
    });
  }

  // Validate email format (simple regex)
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/i.test(email);
  }

  // Show visual feedback using Bootstrap validation styles
  function showValidationFeedback(input, isValid, message = '') {
    if (!input) return;

    const feedback = input.nextElementSibling;
    if (isValid) {
      input.classList.add('is-valid');
      input.classList.remove('is-invalid');
      if (feedback) feedback.textContent = '';
    } else {
      input.classList.add('is-invalid');
      input.classList.remove('is-valid');
      if (feedback) feedback.textContent = message || 'Invalid input';
    }
  }

  // Validate authenticated user's profile form fields (Step 1)
  function validateProfileFormFields() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;

    const firstNameInput = form.querySelector('#first_name');
    const lastNameInput = form.querySelector('#last_name');
    const emailInput = form.querySelector('#email');

    const firstName = firstNameInput?.value.trim();
    const lastName = lastNameInput?.value.trim();
    const email = emailInput?.value.trim();

    const firstValid = !!firstName;
    const lastValid = !!lastName;
    const emailValid = isValidEmail(email);

    showValidationFeedback(firstNameInput, firstValid, 'First name is required.');
    showValidationFeedback(lastNameInput, lastValid, 'Last name is required.');
    showValidationFeedback(emailInput, emailValid, 'Please enter a valid email address.');

    return firstValid && lastValid && emailValid;
  }

  // Validate required billing fields and country-specific postcode format
  function validateBillingFormFields() {
    const form = document.getElementById('billing-form');
    if (!form) return false;

    // Map of required field IDs to error messages
    const requiredFields = {
      billing_street1: 'Street address is required.',
      billing_city: 'City is required.',
      billing_postcode: 'Postcode is required and must be valid.',
      billing_country: 'Country is required.',
      billing_phone: 'Phone number is required.',
    };

    let allValid = true;

    Object.entries(requiredFields).forEach(([id, message]) => {
      const input = form.querySelector(`#${id}`);
      const value = input?.value.trim();
      let isValid = value !== '';

      if (id === 'billing_postcode') {
        const country = form.querySelector('#billing_country')?.value;
        isValid = validatePostalCode(value, country);
      }

      showValidationFeedback(input, isValid, message);
      if (!isValid) allValid = false;
    });

    return allValid;
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

  // Validate required guest fields and email format during step 1
  function validateGuestFormFields() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;

    const firstNameInput = form.querySelector('#first_name');
    const lastNameInput = form.querySelector('#last_name');
    const emailInput = form.querySelector('#email');

    const firstName = firstNameInput?.value.trim();
    const lastName = lastNameInput?.value.trim();
    const email = emailInput?.value.trim();

    const firstValid = !!firstName;
    const lastValid = !!lastName;
    const emailValid = isValidEmail(email);

    showValidationFeedback(firstNameInput, firstValid, 'First name is required.');
    showValidationFeedback(lastNameInput, lastValid, 'Last name is required.');
    showValidationFeedback(emailInput, emailValid, 'Please enter a valid email address.');

    return firstValid && lastValid && emailValid;
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

        // Set progress bar to Step 2
        setActiveProgressStep(2);

        // Reset redirect flag
        continueBtn.disabled = false;
        continueBtn.dataset.allowRedirect = "false";

        // Capture original values for change tracking
        captureInitialFormValues();

        // Set up modal logic for billing changes
        ['billing_street1', 'billing_postcode', 'billing_city', 'billing_country', 'billing_phone'].forEach(id => {
          const input = document.getElementById(id);
          if (input) {
            input.addEventListener('input', () => {
              const isValid = validateBillingFormFields();
              continueBtn.disabled = !isValid;
              continueBtn.dataset.allowRedirect = "false";
              skipProfileSave = false;
            });

            input.addEventListener('blur', () => {
              validateBillingFormFields();
            });
          }
        });

        continueBtn.disabled = !validateBillingFormFields();

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

      if (form.id === 'checkout-profile-form' && !isValidEmail(email)) {
        modalAlert.classList.remove('d-none');
        modalAlert.textContent = "Please enter a valid email address.";
        return;
      }

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
      loadBillingForm();
      return;
    }

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
        <form id="checkout-profile-form" novalidate>
          <input type="hidden" name="csrfmiddlewaretoken"
            value="${document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''}">

          <div class="mb-3">
            <label for="first_name" class="form-label" id="label-first-name">First Name</label>
            <input type="text" class="form-control" name="first_name" id="first_name"
              aria-label="First Name" aria-labelledby="label-first-name" value="${document.body.dataset.firstName || ''}" required>
            <div class="invalid-feedback">First name is required.</div>
          </div>

          <div class="mb-3">
            <label for="last_name" class="form-label" id="label-last-name">Last Name</label>
            <input type="text" class="form-control" name="last_name" id="last_name"
              aria-label="Last Name" aria-labelledby="label-last-name" value="${document.body.dataset.lastName || ''}" required>
            <div class="invalid-feedback">Last name is required.</div>
          </div>

          <div class="mb-3">
            <label for="email" class="form-label" id="label-email">Email</label>
            <input type="email" class="form-control" name="email" id="email"
              aria-label="Email address" aria-labelledby="label-email" value="${document.body.dataset.email || ''}" required>
            <div class="invalid-feedback">Please enter a valid email address.</div>
          </div>
        </form>
      </div>
    `;

    formWrapper.style.display = 'block';

    // Real-time validation listeners for profile form
    ['first_name', 'last_name', 'email'].forEach(id => {
      const input = document.getElementById(id);
      if (input) {
        input.addEventListener('input', () => {
          validateProfileFormFields();
          continueBtn.disabled = !validateProfileFormFields();
          continueBtn.dataset.allowRedirect = "false";
          skipProfileSave = false;
        });

        input.addEventListener('blur', () => {
          validateProfileFormFields();
        });
      }
    });

    continueBtn.disabled = !validateProfileFormFields();
    captureInitialFormValues();
  }

  // Handle login and guest actions
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

          continueBtn.disabled = !validateGuestFormFields();

          // Real-time validation listeners for user_form when guest
          ['first_name', 'last_name', 'email'].forEach(id => {
            const input = document.getElementById(id);
            if (input) {
              input.addEventListener('input', () => {
                validateGuestFormFields();
                continueBtn.disabled = !validateGuestFormFields();
                continueBtn.dataset.allowRedirect = "false";
                skipProfileSave = false;
              });

              input.addEventListener('blur', () => {
                validateGuestFormFields();
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
