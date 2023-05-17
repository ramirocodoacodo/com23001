const app = new Vue({
    el: '#app',
    data: {
        info: {},
        time: ""
    },
    created() {
        fetch('https://api.coindesk.com/v1/bpi/currentprice.json')
        .then(response => response.json())
        .then(data => { 
            console.log(data);
            this.info=data.bpi
            this.time=data.time.updated
            })
        .catch( error => console.log(error));
    }
});
