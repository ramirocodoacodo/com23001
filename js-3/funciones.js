function sumar(num1, num2, num=0) {
    let suma = num1 + num2 + num;
    return suma;
    // console.log("No se alcanza...");
}

function mostrar(texto) {
    console.log(texto);
}

var mostrarA = function (texto) {
    console.log(texto);
}

resultado = sumar(10,2);
console.log("El resultado es:", sumar(10,3));
console.log("El resultado es:", sumar(10,3,2));

console.clear();

// Parámetros por defecto
var a = 5;
// var a = 11;
if (a==5) {
    let a = 4;
    var b = 10;
    // let b = 10;
}
console.log(a);
console.log(b);
salida = mostrar(sumar(2,2));
console.log(salida);  // undefined

console.clear();
// función flecha
var sumarFlecha = (num1, num2) => num1 + num2;
mostrar(sumarFlecha(10,2));

// función anónima
let sumarAnonima = function (num1, num2, num=0) {
    let suma = num1 + num2 + num;
    return suma;
    // console.log("No se alcanza...");
}

mostrar(sumarAnonima(10,2));
mostrar(sumarAnonima);

console.clear();

// callbacks
function procesarEntrada(callback) {
    let nombre = prompt("Ingrese su nombre:");
    callback(nombre);
}

procesarEntrada(mostrarA);

// clousures
function crearFuncion(x){
    return function (num) {
        return num + x;
    }
}

var sumar5 = crearFuncion(5);
var sumar10 = crearFuncion(10);
console.log(sumar5);
console.log(sumar10);
console.log(sumar5(10));
console.log(sumar10(10));
