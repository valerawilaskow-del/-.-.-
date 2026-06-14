// Простой скрипт для страницы seat.html

const zonesList = document.getElementById('zones-list');
const proceedBtn = document.getElementById('proceedToBookingBtn');
const proceedBtnLink = proceedBtn.querySelector('button');
const proceedBtnPrice = proceedBtn.querySelector('strong');
const proceedBtnZone = proceedBtn.querySelector('span');

zonesList.addEventListener('click', function(event) {
   const target = event.target.closest('li');
   if (!target) return; // Если клик не по зоне

   // Снимаем класс active со всех зон
   zonesList.querySelectorAll('li').forEach(li => li.classList.remove('active'));
   // Добавляем класс active к выбранной зоне
   target.classList.add('active');

   // Получаем данные из атрибутов li
   const zoneId = target.getAttribute('data-zone-id');
   const price = target.getAttribute('data-price');
   const name = target.getAttribute('data-name');

   // Обновляем текст кнопки перехода к бронированию
   proceedBtnPrice.textContent = price + ' ₽';
   proceedBtnZone.textContent = name || 'Зона ' + zoneId.toUpperCase();

   // Включаем кнопку и ссылку
   proceedBtn.style.display = 'block';
   proceedBtnLink.disabled = false;
});