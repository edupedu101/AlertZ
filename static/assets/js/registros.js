const app = Vue.createApp({
    data(){
        return {     
            indice: 0,      
            id_sensor: '',
            nombre_sensor: '',
            sensores: [],
            registros: [],

        };
    },

    methods: {
        get_sensores(){
            fetch(`/api/sensores`,{method: 'GET'})
            .then(response => response.json())
            .then((res) =>{
                this.sensores = res.data;
            })
        },
        get_registros(){
            fetch(`/api/registros/${this.id_sensor}`, {method: 'GET'})
            .then(response => response.json())
            .then((res) => {
                this.registros = res.data;
            })
        },
        get_nombre_sensor(){
            this.nombre_sensor = this.sensores[this.indice].nombre;   
        },
        
        set_anterior(){
            if(this.indice  <= 0){
                
            }else{
                this.indice--;
                this.id_sensor = sensores[this.indice].id;
                this.get_registros();}
        },
        set_siguiente() {
            if(this.indice  >= len(this.sensores)){

            }else{
                this.indice++;
                this.id_sensor = sensores[this.indice].id;
                this.get_registros();
                this.get_nombre_sensor();
            }
        },
        
    },
    mounted() {
            this.get_sensores();
            this.id_sensor = sensores[this.indice].id;
            this.get_registros();
            this.get_nombre_sensor();
    
      }
});
const root = app.mount('#app')