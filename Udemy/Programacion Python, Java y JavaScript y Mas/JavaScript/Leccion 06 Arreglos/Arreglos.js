

//let autos = new Array("BMW","Volvo","Mercedes Benz");

// Creacion de un Arreglo

const autos = ["BMW","Volvo","Mercedes Benz"];

console.log(autos); 

// Mostrando valores de un Arreglo

console.log(autos[0]);

for (let i = 0; i < autos.length; i ++){
    console.log(i + " : " + autos[i]) 
}

// Modificar valores de un Arreglo

autos[0] = "Ferrari"
console.log(autos[0]);

// Agregando elementos a un Arreglos

autos.push("Audi");

console.log(autos);

// Length : para mirar la longitud de un arreglo

console.log(autos.length);

autos[autos.length] = "Cadillac";

console.log(autos);

// Agregar elem, independiente si esta lleno o no, se agrega un vacio.

autos[6] = "Porshe"

console.log(autos);

console.log(typeof autos);

// Formas de verificar que es un arreglo.

console.log(Array.isArray(autos));

console.log( autos instanceof Array);