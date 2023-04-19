/*
console.clear();
console.log("Estructuras condicionales");
var num = parseInt(prompt("Ingrese un número: "));
// Condicional simple
if (num > 0) {
    alert("El número es positivo.");
}

// Condicional doble
if (num > 0) {
    alert("El número es positivo.");
}
else {
    alert("El número es negativo o cero.");
}

// Condicional anidado
if (num > 0) 
    alert("El número es positivo.");

else {
    if (num < 0) alert("El número es negativo.");
    else
        alert("El número es cero.");
}

// else-if: elif (NO existe en JS)
if (num > 0)
    alert("El número es positivo.");
else if (num < 0)
    alert("El número es negativo.");
else
    // Indentación
    alert("El número es cero.");
*/
console.clear();

// Switch
// menu = parseInt...
menu = 1;

// Condicional múltiple
switch (menu) {
    case 1:
        console.log("Opción 1: Alta de usuario.");
        break;
    case 2:
    case 3:
        console.log("Opción 2: Baja de usuario.");
        break;
    default:
        console.log("Debe ingresar una opción válida.")
}

// Operadores ternarios
num = 2;
resultado = num > 0 ? "Positivo" : "Negativo o cero";
console.log(num > 0 ? "Positivo" : "Negativo o cero");
console.log(resultado);
