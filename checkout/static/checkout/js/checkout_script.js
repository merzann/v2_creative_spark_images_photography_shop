document.addEventListener('DOMContentLoaded', function () {
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";
  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');
  const downloadButtons = document.querySelectorAll('.download-link');

  let formInitialData = {};
  let skipProfileSave = false;
  let currentStep = 1;

  // Updates the progress UI to indicate the current step
  function setActiveProgressStep(stepNumber) {
    const steps = document.querySelectorAll('.progress-steps .step');
    steps.forEach((stepEl, index) => {
      stepEl.classList.toggle('step-active', index === stepNumber - 1);
    });
    currentStep = stepNumber;
  }

  //Spinner Handler
  function showInlineSpinner(message = 'Please wait...') {
    formWrapper.innerHTML = `
      <div class="text-center my-5">
        <div class="spinner-border text-secondary" role="status" aria-label="${message}"></div>
        <p class="mt-3">${message}</p>
      </div>
    `;
    formWrapper.style.display = 'block';
  }

  function restoreFormWrapper() {
    formWrapper.style.display = 'block';
  }

  // Validates email format using a regular expression
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/i.test(email);
  }

  // Applies visual feedback for input validation
  function showValidationFeedback(input, isValid, message = '') {
    if (!input) return;
    const feedback = input.nextElementSibling;
    input.classList.toggle('is-valid', isValid);
    input.classList.toggle('is-invalid', !isValid);
    if (feedback && !isValid) feedback.textContent = message;
  }

  // Validates profile form fields (name and email)
  function validateProfileFormFields() {
    const form = document.getElementById('checkout-profile-form');
    if (!form) return false;
    const firstNameInput = form.querySelector('#first_name');
    const lastNameInput = form.querySelector('#last_name');
    const emailInput = form.querySelector('#email');

    const firstValid = !!firstNameInput?.value.trim();
    const lastValid = !!lastNameInput?.value.trim();
    const emailValid = isValidEmail(emailInput?.value.trim());

    showValidationFeedback(firstNameInput, firstValid, 'First name is required.');
    showValidationFeedback(lastNameInput, lastValid, 'Last name is required.');
    showValidationFeedback(emailInput, emailValid, 'Please enter a valid email address.');

    return firstValid && lastValid && emailValid;
  }

  // Validates billing form input fields
  function validateBillingFormFields() {
    const form = document.getElementById('billing-form');
    if (!form) return false;

    const requiredFields = {
      billing_street1: 'Street address is required.',
      billing_city: 'City is required.',
      billing_postcode: 'Postcode is required and must be valid.',
      billing_country: 'Country is required.',
      billing_phone: 'Phone number is required.',
    };

    let allValid = true;

    for (const [id, message] of Object.entries(requiredFields)) {
      const input = form.querySelector(`#${id}`);
      let isValid = input?.value.trim() !== '';
      if (id === 'billing_postcode') {
        const country = form.querySelector('#billing_country')?.value;
        isValid = validatePostalCode(input?.value.trim(), country);
      }
      showValidationFeedback(input, isValid, message);
      if (!isValid) allValid = false;
    }

    return allValid;
  }

  // Validates postcode by country format rules
  function validatePostalCode(postcode, country) {
    const rules = {
      IE: /^[A-Z]{1}[0-9]{2}\s?[A-Z0-9]{4}$/i,
      DE: /^\d{5}$/,
      AT: /^\d{4}$/,
      US: /^\d{5}(-\d{4})?$/,
      GB: /^[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2}$/i,
    };
    const regex = rules[country] || /^[A-Z0-9\s\-]{3,10}$/;
    return regex.test(postcode);
  }

  // Alias for validating profile during guest checkout
  function validateGuestFormFields() {
    return validateProfileFormFields();
  }

  // Stores form data to compare later for unsaved changes
  function captureInitialFormValues() {
    const form = document.querySelector('form');
    if (!form) return;
    formInitialData = {};
    new FormData(form).forEach((value, key) => {
      formInitialData[key] = value;
    });
  }

  // Resets form to last captured state
  function resetFormToInitialValues() {
    const form = document.querySelector('form');
    if (!form) return;
    for (const [key, value] of Object.entries(formInitialData)) {
      const field = form.querySelector(`[name="${key}"]`);
      if (field) field.value = value;
    }
  }

  // Detects if form data has changed since last capture
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

  // Loads billing form and attaches validation handlers
  function loadBillingForm() {
    showInlineSpinner('Saving your details...');

    fetch('/checkout/load-billing-form/')
      .then(response => response.text())
      .then(html => {
        formWrapper.innerHTML = html;
        setActiveProgressStep(2);

        // Wait for DOM and browser to populate values before capturing
        setTimeout(() => {
          captureInitialFormValues();
        }, 50); // short delay to let form hydrate


        ['billing_street1', 'billing_postcode', 'billing_city', 'billing_country', 'billing_phone'].forEach(id => {
          const input = document.getElementById(id);
          if (input) {
            input.addEventListener('input', () => {
              const valid = validateBillingFormFields();
              continueBtn.disabled = !valid;
              continueBtn.dataset.allowRedirect = "false";
              skipProfileSave = false;
            });
            input.addEventListener('blur', validateBillingFormFields);
          }
        });

        continueBtn.disabled = !validateBillingFormFields();
      })
      .catch(error => console.error("Billing form load failed:", error));
  }

  function loadCheckoutSummary() {
    showInlineSpinner('Saving your details...');

    fetch('/checkout/summary/')
      .then(response => response.text())
      .then(html => {
        formWrapper.innerHTML = html;
        formWrapper.style.display = 'block';

        // Step 3: Order Summary
        setActiveProgressStep(3);

        // Update button label to Secure Payment
        continueBtn.innerHTML = '<i class="fa fa-lock me-1"></i>Secure Payment';
        continueBtn.disabled = false;
        continueBtn.classList.add('btn-custom');

        // Attach Stripe Checkout handler to the button
        continueBtn.onclick = function () {
          // Step 4: Payment
          setActiveProgressStep(4);

          showInlineSpinner('Saving your details...');

          fetch('/checkout/create-checkout-session/', {
            method: "POST",
            headers: {
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')?.value,
              'Content-Type': 'application/json'
            },
          })
          .then(res => res.json())
          .then(session => {
            const stripe = Stripe(document.body.dataset.stripePublicKey);
            return stripe.redirectToCheckout({ sessionId: session.id });
          })
          .then(result => {
            if (result.error) {
              alert(result.error.message);
            }
          })
          .catch(error => console.error("Error launching Stripe Checkout:", error));
        };
      })
      .catch(error => console.error('Error loading summary:', error));
  }

  // Profile save logic attached to save button in modal
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

      showInlineSpinner('Saving your details...');

      fetch(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrfToken },
        body: formData,
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          const modalInstance = bootstrap.Modal.getInstance(document.getElementById('saveModal'));
          modalInstance.hide();

          setTimeout(() => {
            captureInitialFormValues();
            if (currentStep === 1) {
              loadBillingForm();
            } else if (currentStep === 2) {
              loadCheckoutSummary();
            }
          }, 300);
        } else {
          throw new Error('Unexpected response');
        }
      })
      .catch(error => {
        modalAlert.classList.remove('d-none');
        modalAlert.textContent = "Unable to save your profile. Please try again.";
        continueBtn.disabled = false;
      });
    }
  });


  // Skip save and proceed logic on Cancel or Skip buttons
  document.addEventListener('click', function (event) {
    if (['skip-save', 'Cancel'].includes(event.target?.id || event.target?.textContent.trim())) {
      skipProfileSave = true;
      continueBtn.dataset.allowRedirect = "true";
      continueBtn.disabled = false;
      if (isAuthenticated) resetFormToInitialValues();
      bootstrap.Modal.getInstance(document.getElementById('saveModal')).hide();
    }
  });

  // Continue button event based on step number
  continueBtn.addEventListener('click', function () {
    const isValid = currentStep === 1
      ? validateProfileFormFields()
      : validateBillingFormFields();

    if (!isValid) {
      continueBtn.disabled = true;
      return;
    }

    if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave === true) {
      if (currentStep === 1) {
        loadBillingForm();
      } else if (currentStep === 2) {
        loadCheckoutSummary();
      }
      continueBtn.blur();
    } else if (formHasChanges()) {
      continueBtn.disabled = true;
      modalAlert.classList.add('d-none');
      saveModal.show();
    } else {
      if (currentStep === 1) {
        loadBillingForm();
        continueBtn.blur();
      } else if (currentStep === 2) {
        loadCheckoutSummary();
        continueBtn.blur();
      }
    }
  });

  // Handles login button redirection with spinner feedback
  if (loginBtn) {
    loginBtn.addEventListener('click', () => {
      const choiceWrapper = document.getElementById('checkout-choice-wrapper');
      const formWrapper = document.getElementById('checkout-form-wrapper');

      choiceWrapper?.classList.add('d-none');

      formWrapper.innerHTML = `
        <div class="text-center my-5">
          <div class="spinner-border text-secondary" role="status" aria-label="Redirecting..."></div>
          <p class="mt-3">Redirecting to login...</p>
        </div>
      `;
      formWrapper.style.display = 'block';

      setTimeout(() => {
        window.location.href = '/accounts/login/?next=/checkout/';
      }, 400);
    });
  }

  // Guest checkout button logic
  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      const choiceWrapper = document.getElementById('checkout-choice-wrapper');
      const formWrapper = document.getElementById('checkout-form-wrapper');

      choiceWrapper?.classList.add('d-none');

      formWrapper.innerHTML = `
        <div class="text-center my-5">
          <div class="spinner-border text-secondary" role="status" aria-label="Redirecting..."></div>
          <p class="mt-3">Redirecting to guest checkout...</p>
        </div>
      `;
      formWrapper.style.display = 'block';

      fetch('/checkout/load-guest-form/')
        .then(res => res.text())
        .then(html => {
          formWrapper.innerHTML = html;
          setActiveProgressStep(1);
          captureInitialFormValues();
          continueBtn.disabled = !validateGuestFormFields();

          ['first_name', 'last_name', 'email'].forEach(id => {
            const input = document.getElementById(id);
            if (input) {
              input.addEventListener('input', () => {
                validateGuestFormFields();
                continueBtn.disabled = !validateGuestFormFields();
                continueBtn.dataset.allowRedirect = "false";
                skipProfileSave = false;
              });
              input.addEventListener('blur', validateGuestFormFields);
            }
          });
        })
        .catch(err => {
          console.error("Failed to load guest form", err);
          formWrapper.innerHTML = '<p class="text-danger">Failed to load the form. Please try again.</p>';
          choiceWrapper?.classList.remove('d-none');
        });
    });
  }

  // Initialize step and validation for authenticated users
  if (isAuthenticated) {
    continueBtn.disabled = !validateProfileFormFields();
    captureInitialFormValues();
    setActiveProgressStep(1);
  }

  // Initialize guest checkout from server-side session flag
  if (!isAuthenticated && document.getElementById('checkout-profile-form')) {
    continueBtn.disabled = !validateGuestFormFields();
    captureInitialFormValues();
    setActiveProgressStep(1);

    ['first_name', 'last_name', 'email'].forEach(id => {
      const input = document.getElementById(id);
      if (input) {
        input.addEventListener('input', () => {
          validateGuestFormFields();
          continueBtn.disabled = !validateGuestFormFields();
          continueBtn.dataset.allowRedirect = "false";
          skipProfileSave = false;
        });
        input.addEventListener('blur', validateGuestFormFields);
      }
    });
  }

  // Handles image download for download button on checkout success page
  downloadButtons.forEach(button => {
    button.addEventListener('click', function (e) {
      e.preventDefault();
      const url = this.getAttribute('data-url');

      const tempLink = document.createElement('a');
      tempLink.href = url;
      tempLink.setAttribute('download', '');
      document.body.appendChild(tempLink);
      tempLink.click();
      document.body.removeChild(tempLink);
    });
  });
});
