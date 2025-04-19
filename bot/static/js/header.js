// Функция для переключения темы
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.classList.contains('dark-theme') ? 'dark' : 'light';
  
    // Переключаем классы для светлой и темной темы
    body.classList.toggle('dark-theme');
  
    // Сохраняем выбранную тему в localStorage
    if (currentTheme === 'light') {
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  
    // Обновляем иконку в кнопке
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    if (body.classList.contains('dark-theme')) {
      themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>'; // Иконка Солнца для светлой темы
    } else {
      themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>'; // Иконка Луны для темной темы
    }
  }
  
  // При загрузке страницы проверяем сохраненную тему
  document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-theme');
      const themeToggleBtn = document.getElementById('theme-toggle-btn');
      themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>'; // Иконка Солнца для светлой темы
    }
  });
  