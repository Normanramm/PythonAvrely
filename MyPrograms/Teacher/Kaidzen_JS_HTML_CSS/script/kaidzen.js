// переменные____________________________________________________________________
console.log("test1")
let a = 6
let b = 5
console.log("test2")
console.log(a++) // увеличивает переменную на единицу
console.log(a + b)
console.log("test3")

const text = `Hello, 
World ${a}` // ковычки на кнопке тильда позволяют переносить текст на другую строку
console.log(text)
console.log(text.length)

//функции на языке JavaScript, а так же методы и процедуры_________________________________
function printHelloWorld() {
    console.log("Вывел из функции printHelloWorld ")
    console.log(Math.random())
    console.log(Math.max(1, 2, 3, 4, 5, 6, 7, 8, 9))
    let q = "1"
    console.log(q + 1) // конкатенация
    console.log(+q + 1) // сложит строку и число
    console.log("----------------------")
}
printHelloWorld()

function printText(name, age) {
    console.log(`Привет ${name} тебе ${age} лет`)
}

printText('Vlad', 35)

function printText2(name2, age2) {
    let nameage = `Кот ${name2} тебе ${age2} месяцев`
    return nameage

}
let name2 = 'Tima'
let age2 = 8
console.log(printText2(name2, age2))
let result = printText2(name2, age2) // можно результат функции засунуть в переменную и манипулировать как надо например alert и т.д

//Массивы_________________________________________________
let array = [1, 2, 3, "qwerty", true, [4, 5, 6]]
console.log(array)
console.log(array[array.length - 1])
console.log(array.push("добавил в конец"))

let array2 = [10, 11, 12, 13, 14]
let str = array2.join("*/*")
console.log(str)
let array3 = str.split("*/*")
console.log(array3)

//Объекты_________________________________________________
let obj = {
    "color": "red",
    "snow": true,
    "numbers": [111, 222, 333]
}
console.log(obj)
console.log(obj["color"]) //вывести ключ
console.log(obj["numbers"][1]) //вывести конкретное значение
console.log(Object.keys(obj)) // вывести ключи

//Условные операторы конструкции
let age = 101
if (age < 18) {
    console.log(`Доступ запрещен ${age} летний!`)
}
else if (age >= 18) {
    console.log('Доступ разрешен!')
} else {
    console.log('Проходи')
}

//Циклы__________________________________________________________
let count = 0
while (count < 5) {
    console.log(count)
    count++
}

let count2 = 5
while (count2 > 2) {
    console.log(count2)
    count2--
}



// в сайте________________________________________________
console.log("этот текст я ввел в kaidzen.js");
// // alert("Текст выведен из kaidzen.js");
elem.innerHTML = "Доступ через id делается через решетку #elem в СSS";
document.getElementsByClassName("elem")[0].innerHTML = "Доступ через class делается через точку .elem в CSS";
