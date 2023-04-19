// Operadores de asignación
cont = 0;
cont += 1;  // cont = cont + 1;
cont -= 1;  // cont = cont - 1;

num = 1;
num *= 2;  // num = num * 2;
console.log(num);
num *= 2;  // num = num * 2;
console.log(num);
num *= 2;  // num = num * 2;
console.log(num);
num *= 2;  // num = num * 2;
console.log(num);

// Operador incremental
cont++;  // cont = cont + 1;

// Operadores relacionales
var A = 5;
var B = 2;
console.log(A == B);  // false
console.log(A != B);  // true
console.log(A >= B);  // true

console.clear();

// Operadores lógicos
// AND: &&, OR; ||; NOT: !
console.log(A >= 5-2*1 && B == 0);  // true && false => false
console.log(true && false && true);  // false
console.log(true && true)  // true
console.log(true || false)  // true
console.log(false || false)  // false
console.log(!(A >= 5-2*1 && B == 0))  // true  // (!false)

// Operadores de cadena
texto1 = "Ramiro";
texto2 = "Escalante Leiva"
texto3 = texto1 + " " + texto2;
console.log(texto3);

texto = "";
texto += texto1;
texto += " ";
texto += texto2;
console.log(texto);
