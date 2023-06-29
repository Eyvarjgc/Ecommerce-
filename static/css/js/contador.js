document.querySelector("#btnsumar").addEventListener('click',sumaruno);
document.querySelector("#btnrestar").addEventListener('click',restaruno);

let contador = 0;

function sumaruno(){

    contador = contador+1;
    document.querySelector("#msgcontador").innerHTML=contador

}
function restaruno(){

    contador = contador-1;
    document.querySelector("#msgcontador").innerHTML=contador

}