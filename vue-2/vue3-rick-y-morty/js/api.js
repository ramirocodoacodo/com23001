const { createApp } = Vue 

// const app = Vue.createApp({
createApp({
        data() {
    return {
        // https://rickandmortyapi.com/api/character/247
        url: 'https://rickandmortyapi.com/api/character/',
        personajes: []
        }
    },
    methods: {
        async fetchData(url) {
            const res = await fetch(url);
            data = await res.json();
            // console.log(data.results);
            this.personajes = data.results;
            // await fetch(url)
            //     .then(response => response.json())
            //     .then(data => {
            //         this.personajes = data.results;
            //         console.log(this.personajes);
            //     } )
            //     .catch( err => {
            //         console.error(err);
            //     })
            }
    },
    async created() {
        await this.fetchData(this.url)
    }
}).mount('#app')
