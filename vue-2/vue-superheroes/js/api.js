

const app = new Vue({
    el: '#app',
    data: {
        info: {},
        squadName:"",
        members:[]
    },
    created() {
        fetch('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
        .then(response => response.json())
        .then(data => { 
            console.log(data);
            this.info=data
            this.squadName=data.squadName;
            this.members=data.members
            })
        .catch( error => console.log(error));
    }
});