document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.exchangerate-api.com/v4/latest/USD')
        .then(response => response.json())
        .then(data => {
            document.getElementById('usd-rub-rate').textContent = data.rates.RUB.toFixed(2);
        })
        .catch(error => console.error('Ошибка:', error));

    fetch('https://api.exchangerate-api.com/v4/latest/EUR')
        .then(response => response.json())
        .then(data => {
            document.getElementById('eur-rub-rate').textContent = data.rates.RUB.toFixed(2);
        })
        .catch(error => console.error('Ошибка:', error));
});
function getWeather(city) {
    const apiKey = '89f5532022b253d797a501a65b3f33f7'; // Замените на ваш ключ API
    const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=ru`;

    fetch(apiUrl)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else if (response.status === 401) {
                throw new Error('Неверный ключ API или истек срок действия ключа.');
            } else {
                throw new Error('Ошибка сервера: ' + response.status);
            }
        })
        .then(data => {
            if (data.main) {
                document.getElementById('weather').textContent = `${data.name}, ${data.main.temp}°C`;
            } else {
                throw new Error('Отсутствуют данные о погоде');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}
function getUserCity() {
    fetch('http://ip-api.com/json')
        .then(response => response.json())
        .then(data => {
            const city = data.city;
            getWeather(city);
        })
        .catch(error => console.error('Ошибка определения города:', error));
}
getUserCity();