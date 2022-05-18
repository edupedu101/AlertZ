const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            caca: "hola"
        }
    }
});
app.mount('#app')