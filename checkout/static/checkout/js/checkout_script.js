document.addEventListener('DOMContentLoaded', function () {
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');
  const isAuthenticated = document.body.dataset.authenticated === "true";
  const modalAlert = document.getElementById('modal-alert');
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');

  let formInitialData = {};
  let skipProfileSave = false;
  let currentStep = 1;

  function setActiveProgressStep(stepNumber) {
    const steps = document.querySelectorAll('.progress-steps .step');
    steps.forEach((stepEl, index) => {
      stepEl.classList.toggle('step-active', index === stepNumber - 1);
    });
    currentStep = stepNumber;
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/i.test(email);
  }

  function showValidationFeedback(input, isValid, message = '') {
    if (!input) return;
    const feedback = input.nextElementSibling;
    input.classList.toggle('is-valid', isValid);
    input.classList.toggle('is-invalid', !isValid);
    if (feedback && !isValid) feedback.textContent = message;
  }

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

  function validateGuestFormFields() {
    return validateProfileFormFields();
  }

  function captureInitialFormValues() {
    const form = document.querySelector('form');
    if (!form) return;
    formInitialData = {};
    new FormData(form).forEach((value, key) => {
      formInitialData[key] = value;
    });
  }

  function resetFormToInitialValues() {
    const form = document.querySelector('form');
    if (!form) return;
    for (const [key, value] of Object.entries(formInitialData)) {
      const field = form.querySelector(`[name="${key}"]`);
      if (field) field.value = value;
    }
  }

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

  function loadBillingForm() {
    fetch('/checkout/load-billing-form/')
      .then(response => response.text())
      .then(html => {
        formWrapper.innerHTML = html;
        setActiveProgressStep(2);
        captureInitialFormValues();

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

        continueBtn.onclick = function () {
          if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave) {
            loadCheckoutSummary();
            continueBtn.blur();
            return;
          }

          if (formHasChanges()) {
            continueBtn.disabled = true;
            modalAlert.classList.add('d-none');
            saveModal.show();
          } else {
            loadCheckoutSummary();
            continueBtn.blur();
          }
        };
      })
      .catch(error => console.error("Billing form load failed:", error));
  }

  function loadCheckoutSummary() {
    fetch('/checkout/summary/')
      .then(response => response.text())
      .then(html => {
        formWrapper.innerHTML = html;
        formWrapper.style.display = 'block';
        setActiveProgressStep(3);

        // Update button to Secure Payment state
        continueBtn.innerHTML = '<i class="fa fa-lock me-1"></i>Secure Payment';
        continueBtn.disabled = false;
        continueBtn.classList.add('btn-custom');
      })
      .catch(error => console.error('Error loading summary:', error));
  }

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
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            bootstrap.Modal.getInstance(document.getElementById('saveModal')).hide();
            continueBtn.dataset.allowRedirect = "true";
            continueBtn.disabled = false;
            modalAlert.classList.add('d-none');
            captureInitialFormValues();
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

  document.addEventListener('click', function (event) {
    if (['skip-save', 'Cancel'].includes(event.target?.id || event.target?.textContent.trim())) {
      skipProfileSave = true;
      continueBtn.dataset.allowRedirect = "true";
      continueBtn.disabled = false;
      if (isAuthenticated) resetFormToInitialValues();
      bootstrap.Modal.getInstance(document.getElementById('saveModal')).hide();
    }
  });

  continueBtn.addEventListener('click', function () {
    if (currentStep === 1) {
      if (continueBtn.dataset.allowRedirect === "true" || skipProfileSave === true) {
        loadBillingForm();
        continueBtn.blur();
      } else if (formHasChanges()) {
        continueBtn.disabled = true;
        modalAlert.classList.add('d-none');
        saveModal.show();
      } else {
        loadBillingForm();
        continueBtn.blur();
      }
    } else if (currentStep === 2) {
      loadCheckoutSummary();
      continueBtn.blur();
    }
  });

  if (loginBtn) {
    loginBtn.addEventListener('click', () => {
      window.location.href = '/accounts/login/?next=/checkout/';
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      fetch('/checkout/load-guest-form/')
        .then(res => res.text())
        .then(html => {
          formWrapper.innerHTML = html;
          formWrapper.style.display = 'block';
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
        });
    });
  }

  if (isAuthenticated) {
    continueBtn.disabled = !validateProfileFormFields();
    captureInitialFormValues();
    setActiveProgressStep(1);
  }
});
