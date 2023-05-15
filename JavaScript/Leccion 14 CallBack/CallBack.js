

// Funciones CallBack (volver a llamar una funcion dentro de una funcion)

// funciones comunes.

function miFuncion(){
    console.log("Funcion 1");
}

function miFuncion2(){
    console.log("Funcion 2");
}

miFuncion();
miFuncion2();

// Funcion tipo callback

function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(ap1,ap2,funcionCallback){
    let res = ap1 + ap2;
    funcionCallback(`Resultado : ${res}`);
}

sumar(5,3,imprimir);

// Llamadas asincronas con uso setTimeout;

function miFuncionCallback(){
    console.log("Hola Mundo! desde Callback, 3 Seg.")
}

setTimeout(miFuncionCallback, 3000); // Despues de 3 seg. 

setTimeout ( function() { console.log("Saludos asincronos 2, 4 Seg")}, 4000);

setTimeout( () => console.log("Saludos asincrono 3, 1 Seg"), 1000);

// Funcion setInterval  

let relog = () => {
    let fecha = new Date();
    console.log(`La Hora es : ${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`)
}

setInterval(relog , 2000); // 2 seg

