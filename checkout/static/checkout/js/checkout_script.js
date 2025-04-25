document.addEventListener('DOMContentLoaded', function () {
    const loginBtn = document.getElementById('btn-login');
    const guestBtn = document.getElementById('btn-guest');
    const formWrapper = document.getElementById('checkout-form-wrapper');
    const continueBtn = document.getElementById('continue-btn');
  
    function loadForm(isGuest) {
      formWrapper.innerHTML = ''; // Clear first
  
      // Simulate loading logic (can be replaced with AJAX)
      formWrapper.innerHTML = `
        <div class="card p-4 shadow-sm">
          <h5 class="mb-3">${isGuest ? 'Guest Checkout' : 'Welcome back!'}</h5>
          <form id="checkout-form">
            <div class="mb-3">
              <label for="email" class="form-label">Email Address</label>
              <input type="email" class="form-control" id="email" placeholder="you@example.com" ${isGuest ? '' : 'value="user@example.com"'}>
            </div>
            <div class="mb-3">
              <label for="name" class="form-label">Full Name</label>
              <input type="text" class="form-control" id="name" placeholder="John Doe" ${isGuest ? '' : 'value="John Doe"'}>
            </div>
          </form>
        </div>
      `;
  
      formWrapper.style.display = 'block';
      continueBtn.disabled = false;
    }
  
    loginBtn.addEventListener('click', function () {
      loadForm(false);
    });
  
    guestBtn.addEventListener('click', function () {
      loadForm(true);
    });
  });
  