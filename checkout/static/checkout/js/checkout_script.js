document.addEventListener('DOMContentLoaded', function () {
  // Select form container and continue button
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');

  // Check if the user is authenticated
  const isAuthenticated = document.body.dataset.authenticated === "true";

  // Modal HTML for confirming profile save
  const modalHtml = `
    <div class="modal fade" id="saveModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Save Changes?</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"
              aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Do you want to save the changes to your profile?</p>
            <div id="modal-alert" class="alert alert-danger d-none" role="alert">
              An error occurred while saving your profile. Please try again.
            </div>
          </div>
          <div class="modal-footer">
            <button id="save-profile" class="btn btn-success">Save</button>
            <button id="skip-save" class="btn btn-warning">Don't Save</button>
            <button class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          </div>
        </div>
      </div>
    </div>`;

  // Inject modal HTML into the document
  document.body.insertAdjacentHTML("beforeend", modalHtml);

  // Initialize Bootstrap modal and alert
  const saveModal = new bootstrap.Modal(document.getElementById('saveModal'));
  const modalAlert = document.getElementById('modal-alert');

  // If user is authenticated, show form with prefilled data
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

    // Enable the Continue button once the form is rendered
    continueBtn.disabled = false;

    // Show modal when Continue is clicked
    continueBtn.addEventListener('click', function () {
      saveModal.show();
    });

    // Save profile and redirect to billing
    document.getElementById('save-profile').addEventListener('click', function () {
      const form = document.getElementById('checkout-profile-form');
      const formData = new FormData(form);

      fetch('/user_profiles/save-profile-from-checkout/', {
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
          modalAlert.textContent =
            "Unable to save your profile. Please try again.";
        });
    });

    // Skip saving and continue to billing
    document.getElementById('skip-save').addEventListener('click', function () {
      window.location.href = '/checkout/billing/';
    });
  }

  // Handle unauthenticated options: login or guest checkout
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');

  if (loginBtn) {
    loginBtn.addEventListener('click', function () {
      // Redirect to login page, then back to checkout after login
      window.location.href = '/accounts/login/?next=/checkout/';
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener('click', function () {
      // Simulate continue action (skipping profile save)
      continueBtn.click();
    });
  }
});
