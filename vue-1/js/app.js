/**
 * Extensiones: 
 * Convetir en Template String un String: https://marketplace.visualstudio.com/items?itemName=meganrogge.template-string-converter
 * Formatear un Template: https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html
 */

// Directivas: https://vuejs.org/api/built-in-directives.html

// Ejemplo 1: Hola Mundo y Conexión View con Model
const ejemplo1 = Vue.createApp({
    data(){
        return{
            mensaje: 'Introducción a Vue.js'
        }
    }
}).mount("#ejemplo1");

// ejemplo1.mensaje = 'Conexión establecida con JS'

// Ejemplo2: métodos e interpolación (Modificación del DOM)
const ejemplo2 = Vue.createApp({
    data(){
        return{
            nombre: "Ramiro",
            apellido: "Escalante Leiva",
            direccion: "Buenos Aires"
        }
    },
    methods: {
        detalles() {
            return `Soy ${this.nombre} ${this.apellido} y vivo en ${this.direccion}`;
        }
    }
}).mount("#ejemplo2");

// Ejemplo3: v-html, v-bind (atributos)
const ejemplo3 = Vue.createApp({
    data(){
        return{
            // contenidoHtml:
            contenidoHtml: /*html*/ `
            <div>
                <h2>Imagen de un paisaje</h2>
            </div>`,
            imgSrc: "img/ironman-vs-cap.jpg",
            imgAlt: "Iron Man vs. Captain America"
        }
    }
}).mount("#ejemplo3");

// Ejemplo 4: template y componentes
const CustomComponent1 = {
    template:   /*html*/`
                <div>
                    <button>{{buttonText}}</button>
                </div>`,
    data() {
        return {
            'buttonText': "Componente Custom en Vue.JS 3"
        }
    }
}

const ejemplo4 = Vue.createApp({
    components: {
        'custom-component-1': CustomComponent1
    }
}).mount("#ejemplo4");

// Ejemplo 5: v-on (eventos: click, mouseover, mouseout), componentes, métodos
const CustomComponent2 = {
    // <div v-on:mouseover = "cambiarNombre();" v-on:mouseout = "reestablecerNombre();">
    template: /*html*/`
                <div v-on:click = "cambiarNombre();" v-on:mouseout = "reestablecerNombre();">
                    <h1>Componente creado por <span id = "nombre">{{nombre}}</span></h1>
                </div>`,
    data(){
        return{
            nombre: "Ramiro"
        }
    },
    methods: {
        cambiarNombre() {
            this.nombre = "Ezequiel";
        },
        reestablecerNombre() {
            this.nombre = "Ramiro";
        }
    }
}

const ejemplo5 = Vue.createApp({
    components: {
        'custom-component-2': CustomComponent2
    }
}).mount("#ejemplo5");

// Ejemplo 6: componente dinámico (sólo si hay tiempo)
const ejemplo6 = Vue.createApp({
    data(){
        return{
            vista: 'componente'
        }
    },
    components: {
        'componente': {
            template: /*html*/`
                        <div>
                            <span style = "font-size:3rem;color:green;">
                                Componente dinámico
                            </span>
                        </div>`
        }
    }
}).mount("#ejemplo6");

// Ejemplo 7: input, v-model (enlace bidireccional), propiedades computadas
const ejemplo7 = Vue.createApp({
    data(){
        return{
            nombre: "",
            apellido: ""
        }
    },
    computed: {
        getNombreCompleto() {
            return this.nombre + " " + this.apellido;
        }
    }
}).mount("#ejemplo7");

// Enlace bidireccional
// ejemplo7.nombre = "Ingrese su nombre..."

// Ejemplo 8: Accediendo a Elementos del DOM utilizando $refs (sólo si hay tiempo)
const ejemplo8 = Vue.createApp({
    methods: {
        addText() {
            const text          = this.$refs.text.value;  // tomo los datos del input
            const textField     = this.$refs.textField;  // y del p para modificarlo
            textField.innerHTML = `${textField.innerHTML}<br>${text}`;  // agrego texto al p
        },
        deleteText() {
            const textField     = this.$refs.textField;
            textField.innerHTML = "";
        }
    }
}).mount("#ejemplo8");

// Ejemplo 9: integración, v-if, v-for (sólo si hay tiempo)
const ejemplo9 = Vue.createApp({
    data(){
        return{
            titulo: "Ejemplo Integrador",
            frutas: [
                { nombre: 'Pera', cantidad: 10 },
                { nombre: 'Manzana', cantidad: 0 },
                { nombre: 'Banana', cantidad: 11 }
            ],
            nuevaFruta: '',
            total: 0
        }
    },
    methods: {
        agregarFruta() {
            this.frutas.push({ nombre: this.nuevaFruta, cantidad: 0 })
            this.nuevaFruta = ''
        },
        otroMetodo() {

        }
    },
    // Propiedad computada
    computed: {
        sumarFrutas() {
            this.total = 0;
            for (fruta of this.frutas) {
                this.total += fruta.cantidad;
            }
            return this.total;
        }
    }
}).mount("#ejemplo9");

// ejemplo9.titulo = 'Integración, v-if, v-for';
