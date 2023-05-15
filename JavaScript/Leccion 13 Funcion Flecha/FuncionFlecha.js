

// 

// miFuncionFlecha(); Las Funciones Flechas no se puede llamar antes de hacer la funcion
// miFuncion(); Las Funciones se puede llamar antes de crear la funcion.


function miFuncion(){
    console.log("Hola Mundo!");
}

// se utiliza const en la creacion de funciones flecha.

const miFuncionFlecha = () => {
    console.log("HolaMundo! desde Flecha")
}

miFuncionFlecha();
miFuncion();

const miFuncionFlecha2 = () => console.log("HolaMundo! desde Flecha 2");

miFuncionFlecha2();

const saludar = () => {
    return "Retorno Saludos desde funcion flecha"
}

console.log( saludar () );

// Simplificada
const saludar2 = () => "Retorno Saludos desde funcion flecha 2";
   
console.log( saludar2 () );


// Regresar un Objeto funcion Flecha

const regresaObjeto = () => ({nombre: "juan", apellido: "lara"})
console.log(regresaObjeto());


// Recivir parametros

const funcionConParametros = (mensaje) => console.log(mensaje);
funcionConParametros("Hola Mundo! con parametro");

// Si es solo 1 parametro se puede utilizar sin ();


