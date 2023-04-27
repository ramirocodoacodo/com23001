var persona = {
    nombre: "Juan",
    edad: 40,
    dni: 1234,
    datosPersona: function() {
        return this.nombre + " tiene " + this.edad + " años."
    }
}

console.log(persona);
console.log(persona.dni);
console.log(persona.toString());
console.log(persona.datosPersona());

class Perro {
    constructor(nombre, edad) {
        this.nombre = nombre
        this.edad = edad
    }
}

var perro1 = new Perro("Lola", 10)
var perro2 = new Perro("Lola", 10)
perro1.nombre = "Toby"
console.log(perro1.nombre);
perro1['nombre'] = 'Popei'
console.log(perro1.nombre);
