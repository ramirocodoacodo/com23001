/*
let cad=""
for(let i=0; i<fotos.length; i++){
   cad=cad+ `<img src="${fotos[i]}" alt="foto">`
}
document.getElementById("fotos").innerHTML=cad
*/
var cad=`
<div class="container">
`
    for(let i=0; i< data.length ; i++){
      cad += `
        <div class="tarjeta">
            <img src="${data[i].image}" alt="foto">
            <div class="cuerpo">
                <h4>nombre: ${data[i].name}</h4>
                <p>Genero: ${data[i].gender}</p>
                <p>Especie: ${data[i].species} </p>
            </div>
        </div>
       `
    }       
cad+=`
    </div>
`    
//document.write(cad)
document.getElementById("fotos").innerHTML=cad
