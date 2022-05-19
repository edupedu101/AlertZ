$(document).ready(function(){
    var numRegistros = getNumRegistros()
})
function getNumRegistros(){
    $.ajax("/api/sensores/registros/numRegistros")
    .then(function(data){
        console.log(data);
        colocarNumRegistros(data.data)
    })

    
    return true
}
function colocarNumRegistros(numRegistros){
    for (let i = 0; i < numRegistros.length; i++) {
        $('table tbody tr:nth-child('+(i+1)+') td:nth-child(4) span').text(numRegistros[i])
    }
}