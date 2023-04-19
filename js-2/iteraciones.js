// Ciclo exacto
var cont = 0;
while (cont < 5) {
    cont++;
    console.log(cont);
}

// Ciclo condicional
// while: mientras
suma = 0;
var num = parseInt(prompt("Ingrese un num: "));
while (num != 0) {
    suma += num;  // suma = suma + num;
    num = parseInt(prompt("Ingrese un num: "));
}
console.log("El resultado de la suma:", suma);

// do-while
do {
    num = parseInt(prompt("Ingrese un num: "));
} while (num != 0);

// for: ciclo exacto
for (let i=1; i<=5; i++) {
    console.log(i);

    // Mala práctica
    if (i==3)
        break;
}
