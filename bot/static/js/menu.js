// Функция для добавления товара в корзину
function addToCart(dish) {
    console.log('[FRONT] Добавление товара в корзину:', dish);

    // Получаем корзину из localStorage или создаем новую, если её нет
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Проверяем, есть ли уже такой товар в корзине
    const existingDishIndex = cart.findIndex(item => item.id === dish.id);

    if (existingDishIndex !== -1) {
        // Если товар уже в корзине, увеличиваем его количество
        cart[existingDishIndex].quantity += 1;
    } else {
        // Если товара нет в корзине, добавляем его
        dish.quantity = 1; // Устанавливаем начальное количество 1
        cart.push(dish);
    }

    // Сохраняем обновленную корзину в localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Обновляем счетчик в интерфейсе (например, на кнопке корзины)
    updateCartCount();

    // Отправляем данные на сервер (если необходимо)
    fetch('/api/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ dish })
    })
    .then(res => res.json())
    .then(data => {
        console.log('[FRONT] Корзина обновлена на сервере:', data);
        alert('Товар добавлен в корзину!');
    })
    .catch(err => {
        console.error('[FRONT] Ошибка при добавлении в корзину на сервере:', err);
        alert('Ошибка при добавлении в корзину!');
    });
}

// Функция для обновления количества товаров в корзине
function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById('cart-count').textContent = cartCount;
}

// Вызываем updateCartCount при загрузке страницы, чтобы отобразить текущее количество товаров в корзине
window.onload = updateCartCount;

// Функция для переключения видимости описания
function toggleDescription(dishId) {
    const description = document.getElementById(`desc-${dishId}`);
    const toggleButton = document.querySelector(`.toggle-desc[data-dish-id="${dishId}"]`);
    
    // Проверяем текущий стиль отображения и меняем его
    if (description.style.display === 'none') {
        description.style.display = 'block';
        toggleButton.innerHTML = 'Свернуть';
    } else {
        description.style.display = 'none';
        toggleButton.innerHTML = 'Развернуть';
    }
}

