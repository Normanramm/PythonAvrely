console.log('Привет, JavaScript!');

// Пример кода
function greet(name) {
    return `Привет, ${name}!`;
}

const message = greet('Мир');
console.log(message);

// Работа с DOM
document.addEventListener('DOMContentLoaded', function() {
    const button = document.createElement('button');
    button.textContent = 'Нажми меня';
    button.onclick = () => alert('Кнопка нажата!');
    document.body.appendChild(button);
});

