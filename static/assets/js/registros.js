const sensor = JSON.parse(document.getElementById('sensor').textContent);
const registros = JSON.parse(document.getElementById('registros').textContent);
const sensores = JSON.parse(document.getElementById('sensores').textContent);

let app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return {       
            id_sensor: '',
            nombre_sensor: '',
            sensores: [],
            registros: [],
            hay_registros: false

        }
    },
    watch:{
        id_sensor:{
            handler(){
                this.actualizar()
            }
        },
        hay_registros(){
            if(registros.length == 0){
                this.hay_registros = false
            }else{
                this.hay_registros = true
            }
        }
    },
    methods:{
        actualizar(){
            this.getRegistros()
            this.getNombreSensor()
        },
        getNombreSensor(){
            fetch(`/api/sensor/${this.id_sensor}/nombre_sensor`, {method: 'GET'})
            .then(response => response.json())
            .then((res) => {
                this.nombre_sensor = res.data
            })
        },
        getRegistros(){
            fetch(`/api/registros/${this.id_sensor}`, {method: 'GET'})
            .then(response => response.json())
            .then((res) => {
                this.registros = res.data;
            })
        },
        set_anterior(){
            let indice = this.sensores.indexOf(this.id_sensor)
            if(indice  == 0){
                this.id_sensor = this.sensores[this.sensores.length -1];
            }else{
                this.id_sensor = this.sensores[indice-1];
                }
        },
        set_siguiente() {
            let indice = this.sensores.indexOf(this.id_sensor)
            if(indice  == this.sensores.length - 1){
                this.id_sensor = this.sensores[0];
            }else{
                this.id_sensor = this.sensores[indice+1];
                
            }
        }
    },
    mounted(){
        this.registros = registros;
        this.id_sensor = sensor.id;
        this.nombre_sensor = sensor.nombre;
        this.sensores = sensores;
    }
})
app.mount('#app')
