


function addToCart(dish) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(dish);
    localStorage.setItem('cart', JSON.stringify(cart));
    alert(`${dish.name} добавлено в корзину.`);
}

function checkLoginStatus() {
    const phoneNumber = localStorage.getItem('phoneNumber');
    const loginLogoutBtn = document.getElementById('login-logout-btn');
    const welcomeMsg = document.getElementById('welcome-message');

    if (phoneNumber) {
        loginLogoutBtn.textContent = 'Выйти';
        welcomeMsg.innerHTML = `Привет, <strong>${phoneNumber}</strong>!`;
    } else {
        loginLogoutBtn.textContent = 'Войти';
        welcomeMsg.innerHTML = '';
    }
}

function toggleLoginLogout() {
    const phoneNumber = localStorage.getItem('phoneNumber');
    if (phoneNumber) {
        localStorage.removeItem('phoneNumber');
        alert("Вы вышли из системы.");
        location.reload();
    } else {
        document.getElementById("registration-form").style.display = "block";
    }
}

function registerUser() {
    const phoneNumber = document.getElementById('phone-number').value;
    if (phoneNumber) {
        localStorage.setItem('phoneNumber', phoneNumber);
        alert("Вы успешно зарегистрировались!");
        window.location.href = "/menu/";
    } else {
        alert("Пожалуйста, введите свой номер телефона.");
    }
}

checkLoginStatus();
  

