

// CONTRUCTORES 

function Persona(nombre,apellido,email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + " " + this.apellido;
     }
}

let padre = new Persona("Juan", "Perez", "Jpperes@mail.com");

console.log(padre);


let madre = new Persona("Laura","Quintero","JuaQuin@mail.com")

console.log(madre);

padre.nombre = "Carlos";

console.log(padre);
console.log(madre);

// Agregar Metodos Contructores a un objetos

console.log(padre.nombreCompleto());
console.log(madre.nombreCompleto());

// Distintas Formas de Contruir un Objeto

let miObjeto = new Object();
let miObjeto2 = {};
console.log(typeof miObjeto);
console.log(typeof miObjeto2);

let miCadena = new String();
let miCadena2 = "Hola";
console.log(typeof miCadena);
console.log(typeof miCadena2);

let miNumero = new Number(1);
let miNumero1 = 1;
console.log(typeof miNumero);
console.log(typeof miNumero1);

let miBoolean = new Boolean(false);
let miBoolean1 = false;
console.log(typeof miBoolean);
console.log(typeof miBoolean1);

let miArreglo = new Array();
let miArreglo1 = [];
console.log(typeof miArreglo);
console.log(typeof miArreglo1);

let miFuncion = new Function();
let miFuncion1 = function(){1};
console.log(typeof miFuncion);
console.log(typeof miFuncion1);

// Uso prototype 
// Podremos modificar atributos y metodos de un objeto.

padre.tel = "021654977"
console.log(padre.tel);
console.log(madre.tel);

Persona.prototype.tel = "000000000";

console.log(padre.tel);
console.log(madre.tel);

// Uso de Call

let persona1 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo,tel){
        return titulo + ": " + this.nombre + " " + this.apellido + " " + tel;
    },
    nombreCompleto: function(){
        return this.nombre + " " + this.apellido;
    }
}

let persona2 = {
    nombre: "Carlos",
    apellido: "Lara"
}

// el metodo de persona1.nombreCompleto con los datos de persona2

console.log(persona1.nombreCompleto());

console.log(persona1.nombreCompleto.call(persona2));

// Argunmentos de Call

console.log(persona1.nombreCompleto2.call(persona2, "Ing" , "13214984"));

// Metodo Aplly
// Se utitlisa un arreglo para pasar 

let arreglo = ["Ing","321654955"]

console.log(persona1.nombreCompleto2("Ing","321654955"));
console.log(persona1.nombreCompleto2.apply( persona2, arreglo ));

