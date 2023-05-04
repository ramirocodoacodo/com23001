const a1 = [1,2,3,-5]
var a2 = []
var a3 = [-1000, 12, "ramiro", true, [1,23]]
a4 = new Array(1,2,3,4,0)

console.log(a3.length)
console.log(a3[a3.length-1].length)

// Métodos
largo = a1.push(100,102)
console.log(largo)
a1.pop()
console.log(a1)

const fruits = ["Banana", "Orange", "Apple", "Mango"];
// delete fruits[0];
nuevoArray = fruits.slice(1,3)

console.log(nuevoArray)

matriz = [
    [1,2,3],
    [0,0,2],
    [1,2,3]
    ];

console.log(matriz[1][2])

console.clear();

var persona = {
    nombre: "Ana",
    apellido: "Paz",
    edad: 25
}

for (let index = 0; index < fruits.length; index++) {
    // fruits[index] = fruits[index][0]
    let element = fruits[index];
    element = element[0];
    console.log(element);
}

for (const key in persona) {
    console.log(key + ": " + persona[key])
}

for (const key in fruits) {
    fruits[key] = fruits[key][0]
}

console.clear();

for (const elem of fruits) {
    console.log(elem);
}

console.log(fruits);

fruits.sort();
fruits.reverse();

puntos = [40, 100, 1, 5, 25];
puntos.sort(function(a,b){return b-a})
console.log(puntos);

function multiplicar(elem, i, arr){
    arr[i] = elem * 10;
}

puntos.forEach(multiplicar);
console.log(puntos);

edades = [7, 17, 18, 20, 50];

function esMayor(e){
    return e >= 18;
}

console.log(edades.some(esMayor));

nuevoArrayEdades = edades.filter(esMayor)
console.log(nuevoArrayEdades)
