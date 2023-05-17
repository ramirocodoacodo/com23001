const {createApp} = Vue;

const app = Vue.createApp({
    data() {
        return {
            titulo1: 'Hola Vue!',
            frutas: [
                {nombre: 'Pera', cantidad: 10},
                {nombre: 'Manzana', cantidad: 0}
            ],
            nuevaFruta:''
        }
    },
    methods: {
        agregarFruta() {
            this.frutas.push({nombre:this.nuevaFruta, cantidad:0});
            this.nuevaFruta = "";
        },
        otroMetodo() {
            
        }
    }
}).mount('#ejemplo9')
