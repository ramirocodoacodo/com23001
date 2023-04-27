var nombre = "Ramiro";
var apellido = new String("Escalante Leiva");
console.log(nombre.length)
console.log(apellido.length)

// Métodos
console.log(nombre.charAt(1));
console.log(nombre[1]);
console.log(nombre.concat(apellido, "."));
console.log(nombre.indexOf("Ra"));
console.log(apellido.split(" "));  // ['Escalante', 'Leiva']

// document
document.write("Hola Mundo!");
document.write(nombre.toLocaleUpperCase() + "<br>")
document.write("Hola Mundo!");
