// переменные____________________________________________________________________
console.log("test1");
let a = 6;
let b = 5;
console.log("test2");
console.log(a++); // увеличивает переменную на единицу
console.log(a + b);
console.log("test3");

const text = `Hello, 
World ${a}`; // кавычки на кнопке тильда позволяют переносить текст на другую строку
console.log(text);
console.log(text.length);

// функции на языке JavaScript, а так же методы и процедуры_________________________________
function printHelloWorld() {
    console.log("Вывел из функции printHelloWorld ");
    console.log(Math.random());
    console.log(Math.max(1, 2, 3, 4, 5, 6, 7, 8, 9));
    let q = "1";
    console.log(q + 1); // конкатенация
    console.log(+q + 1); // сложит строку и число
    console.log("----------------------");
}
printHelloWorld();

function printText(name, age) {
    console.log(`Привет ${name} тебе ${age} лет`);
}
printText('Vlad', 35);

function printText2(name2, age2) {
    let nameage = `Кот ${name2} тебе ${age2} месяцев`;
    return nameage;
}
let name2 = 'Tima';
let age2 = 8;
console.log(printText2(name2, age2));
let result = printText2(name2, age2);

// Массивы_________________________________________________
let array = [1, 2, 3, "qwerty", true, [4, 5, 6]];
console.log(array);
console.log(array[array.length - 1]);
console.log(array.push("добавил в конец"));

let array2 = [10, 11, 12, 13, 14];
let str = array2.join("*/*");
console.log(str);
let array3 = str.split("*/*");
console.log(array3);

// Объекты_________________________________________________
let obj = {
    "color": "red",
    "snow": true,
    "numbers": [111, 222, 333]
};
console.log(obj);
console.log(obj["color"]);
console.log(obj["numbers"][1]);
console.log(Object.keys(obj));

// Условные операторы конструкции
let age = 101;
if (age < 18) {
    console.log(`Доступ запрещен ${age} летний!`);
} else if (age >= 18) {
    console.log('Доступ разрешен!');
} else {
    console.log('Проходи');
}

// Циклы__________________________________________________________
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

let count2 = 5;
while (count2 > 2) {
    console.log(count2);
    count2--;
}

// DOM на JavaScript(будет работать до script)_______________________________________

// textContent - текстовое содержимое элемента
// querySelector() - найти элемент по CSS селектору
// nodeList - список из элементов (похож на массив)
// getElementById() - найти элемент по идентификатору
// innerHTML - содержимое элемента с HTML тегами


// Для HTML
// 1. Работа с element5
let elem5 = document.getElementById('element5');
elem5.textContent += " (А этот добавил в kaidzen.js для DOM)";
elem5.style.background = "green"; // Меняем цвет фона на зеленый
elem5.style.color = "white";      // Меняем цвет текста на белый


// 2. Работа с element6
let elem6 = document.getElementById('element6');
// Здесь используем innerHTML, так как внутри есть HTML-тег <b>
elem6.innerHTML += " <b style='color: yellow'> (А этот цвет шрифта изменил в kaidzen.js для DOM c использованием стиля)</b>";
elem6.style.background = "blue";   // Меняем цвет фона на красный
elem6.style.color = "#00ffbb";


// // второй вариант, но лучше использовть тот, что выше!!!
// element6.innerHTML += " <b style='color: yellow'> А этот добавил в kaidzen.js для DOM второй вариант написания)</b>"; // Меняем текст 
// element6.style.background = "red" // меняем цвет фона
// element6.style.color = "white" // меняем цвет текста


// 3. Работа только с element7 (убираем предыдущие наложения!)
// Мы выбираем только те div, у которых есть класс 'element7' (точка перед именем обязательна!)
let elems7 = document.querySelectorAll('.element7');

for (let i of elems7) {
    i.innerHTML += " <b style='color: #70f8ad'> (А этот цвет шрифта изменил в kaidzen.js для DOM c использованием стиля и циклом for)</b>";
    i.style.background = "red";
    i.style.color = "white";
}

// 4. С циклом while
let elems8 = document.querySelectorAll('.element8');
let i = 0;
while (i < elems8.length) {
    elems8[i].innerHTML += " <b style='color: #f870eb'> (А этот цвет шрифта изменил в kaidzen.js для DOM c использованием стиля и циклом while)</b>";
    elems8[i].style.background = "green";
    elems8[i].style.color = "white";
    i++;
}


// 5. Работа с массивом, для отображения на странице
let strs = ["Элемент 1 (созданно)", "Элемент 2(в kaidzen.js)", "Элемент 3(для DOM)"];
document.querySelector('.element9').innerHTML = `
<ol>
    <li style="background: yellow;">${strs[0]} (этот будет синим)</li>
    <li style="color: blue;">${strs[1]} (этот будет синим)</li>
    <li style="color: green;">${strs[2]} (этот будет красным)</li>
</ol>
`

let strs2 = ["Элемент 4 (созданно)", "Элемент 5(в kaidzen.js)", "Элемент 6(для DOM)"];
document.querySelector('.element10').innerHTML = `
${strs2[0]} - ${strs2[1]} - ${strs2[2]}
`


// // Если вы хотите управлять стилями исключительно через JS, менять их нужно после того, как innerHTML сгенерировал HTML-код, иначе JS не найдет элементы внутри.
// let strs = ["Элемент 1 (создано)", "Элемент 2 (в kaidzen.js)", "Элемент 3 (для DOM)"];

// // 1. Сначала вставляем HTML
// const container = document.querySelector('.element9');
// container.innerHTML = `
// <ol>
//     <li>${strs[0]}</li>
//     <li>${strs[1]}</li>
//     <li>${strs[2]}</li>
// </ol>
// `;

// // 2. Затем находим сам список (ol) внутри контейнера и красим его
// const listElement = container.querySelector('ol');
// listElement.style.color = "red"; 

// // Или красим конкретный элемент (например, второй <li>):
// const secondItem = container.querySelectorAll('li')[1];
// secondItem.style.color = "green";



// Атрибуты в DOM___________________________________________________
let element_proverka = document.querySelector('.element10')
element_proverka.setAttribute('title', 'изменил всплывающую подсказу в kaidzen.js')

console.log(element_proverka.hasAttribute('title')) // поиск атрибута
console.log(element_proverka.getAttribute('title')) // позволяет получить значение определенного атрибута
console.log(element_proverka.dataset.about) // для взаимодействия со свои атрибутом, если он составной(data-about-block в HTML коде), то пишется - element_proverka.dataset.aboutBlock


// Для калькулятора в DOM________________________________________________
function update() {
    let money = +document.querySelector('.money').value // с помощью плюса превратили в число
    let year = +document.querySelector('.year').value   // с помощью плюса превратили в число
    let result2 = money + money * 0.12 * year
    document.querySelector('.result2').textContent = result2
}

update()

document.querySelector('.money').addEventListener('input', update)

document.querySelector('.year').addEventListener('input', update)

// Вариант написания с анонимной функцией
// document.querySelector('.monye').addEventListener('input', function () {
//     update()
// })

// document.querySelector('.year').addEventListener('input', function () {
//     update()
// })


// Для CSS 
let elem = document.querySelector("#element6")


// в сайте________________________________________________
console.log("этот текст я ввел в kaidzen.js");
// alert('Это простое сообщение вылезет при запуске сайта!');

// ВНИМАНИЕ: innerHTML перезапишет то, что мы сделали через textContent выше! 
// Если хочешь видеть оба варианта, меняй разные элементы.
// elem.innerHTML = "Доступ через id делается через решетку #elem в CSS";

document.getElementsByClassName("elem")[0].innerHTML = "Доступ через class делается через точку .elem в CSS";
