function toggleLoginLogout() {
    const phone = localStorage.getItem('phoneNumber');
    if (phone) {
      localStorage.removeItem('phoneNumber');
      showToast("Шумо баромадед.");
      location.reload();
    } else {
      const modal = new bootstrap.Modal(document.getElementById('loginModal'));
      modal.show();
    }
  }
  
  function submitPhone() {
    const input = document.getElementById('phoneInput').value;
    if (input) {
      localStorage.setItem('phoneNumber', input);
      showToast("Бомуваффақият ворид шудед!");
      location.reload();
    }
  }
  
  function toggleTheme() {
    const body = document.body;
    const currentTheme = body.classList.contains('dark-theme') ? 'dark' : 'light';
  
    if (currentTheme === 'light') {
      body.classList.add('dark-theme');
      localStorage.setItem('theme', 'dark');
    } else {
      body.classList.remove('dark-theme');
      localStorage.setItem('theme', 'light');
    }
  }
  
  function showToast(message) {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'toast align-items-center text-bg-success border-0 show';
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    toast.innerHTML = `
      <div class="d-flex">
        <div class="toast-body">${message}</div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
      </div>`;
    container.appendChild(toast);
  
    setTimeout(() => toast.remove(), 4000);
  }
  
  function animateCart() {
    const icon = document.getElementById('cart-icon');
    icon.classList.add('animate__animated', 'animate__tada');
    setTimeout(() => icon.classList.remove('animate__animated', 'animate__tada'), 1000);
  }
  
  window.onload = function () {
    const phone = localStorage.getItem('phoneNumber');
    const loginBtn = document.getElementById('login-logout-btn');
    if (loginBtn) {
      loginBtn.textContent = phone ? 'Выйти' : 'Войти';
    }
  
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-theme');
    }
  
    const langSelector = document.getElementById('langSelector');
    const savedLang = localStorage.getItem('lang') || 'tg';
    langSelector.value = savedLang;
    langSelector.addEventListener('change', () => {
      localStorage.setItem('lang', langSelector.value);
      location.reload();
    });
  };
  