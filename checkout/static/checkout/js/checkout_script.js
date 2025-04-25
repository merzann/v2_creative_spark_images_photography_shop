document.addEventListener('DOMContentLoaded', function () {
  const loginBtn = document.getElementById('btn-login');
  const guestBtn = document.getElementById('btn-guest');
  const formWrapper = document.getElementById('checkout-form-wrapper');
  const continueBtn = document.getElementById('continue-btn');

  if (!loginBtn || !guestBtn) return; // Stop if user is already logged in

  function loadForm(isGuest) {
    formWrapper.innerHTML = ''; // Clear first

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';

    formWrapper.innerHTML = `
      <div class="card p-4 shadow-sm">
        <h5 class="mb-3">${isGuest ? 'Guest Checkout' : 'Log in to your Account'}</h5>
        <form method="POST" action="${isGuest ? '/checkout/billing/' : '/accounts/login/?next=/checkout/billing/'}" id="checkout-form">
          <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
          ${isGuest ? `
            <div class="mb-3">
              <label for="email" class="form-label">Email address</label>
              <input type="email" class="form-control" id="email" name="email" placeholder="you@example.com" required>
            </div>
          ` : `
            <div class="mb-3">
              <label for="id_username" class="form-label">Email address</label>
              <input type="text" class="form-control" name="username" id="id_username" placeholder="you@example.com" required>
            </div>
            <div class="mb-3">
              <label for="id_password" class="form-label">Password</label>
              <input type="password" class="form-control" name="password" id="id_password" placeholder="••••••••" required>
            </div>
          `}
          <button type="submit" class="btn btn-custom mt-2">${isGuest ? 'Continue ➡' : 'Login & Continue ➡'}</button>
        </form>
      </div>
    `;

    formWrapper.style.display = 'block';
    continueBtn.disabled = true;
  }

  loginBtn.addEventListener('click', () => loadForm(false));
  guestBtn.addEventListener('click', () => loadForm(true));
});