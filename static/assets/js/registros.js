const app = Vue.createapp({
    data(){
        return {           
            id_sensor: '',
            nombre_sensor: '',
            sensores: [],
            registros: [],

        };
    },

    methods: {
        get_registros(){
            fetch(`/api/registros/${this.id_sensor}`, {method: 'GET'})
            .then(response => response.json())
            .then((res) => {
                this.registros = res.data;
            })
        },
        get_nombre_sensor(){
            fetch(`/api/sensor/${this.id_sensor}`,{method: 'GET'})
            .then(response => response.json())
            .then((res) => {
                this.nombre_sensor = res.data;
            })
        },
        get_sensores(){
            
        }
        ,
        set_anterior(){
            if(this.id_alumno > 0){
                this.id_alumno--;
                this.get_registros();
            }
        },
        set_siguiente() {
            this.id_alumno++;
            
        },
        
    }
});
const root = app.mount('#app')