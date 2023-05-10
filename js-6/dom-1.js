function cambiarTexto() {
    var elementos = document.getElementsByClassName("ejemplo");
    elementos[0].innerHTML = "Hola!";
}

function cambiarTodos() {
    var elementos = document.getElementsByClassName("ejemplo");
    for (let index = 0; index < elementos.length; index++) {
        const element = elementos[index];
        element.innerHTML = "Hola!";
    }
}

var elementos = document.getElementsByClassName("ejemplo");
elementos[0].innerHTML = "Hola!";
