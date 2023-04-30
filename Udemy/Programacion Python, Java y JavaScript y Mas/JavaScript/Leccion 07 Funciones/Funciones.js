// Se puede llamar la funcion independientemente del lugar ( Hoisting )

miFuncion(6,3);

//Declaracion de funcion

function miFuncion(a,b){    
    console.log("suma : " + (a + b));
}

// Lamando la Funcion

miFuncion(2,3);

// Return regresa el resultado.

function miFuncion2(a,b){
    console.log(arguments.length);    
    return a + b;
}

let resultado = miFuncion2(2,3);
console.log(resultado);

// Guardando funciones en variables. 
// Metodo declaracion linial.

let x = function (a,b){return a+b};

resultado = x(3,3);
console.log(resultado);

(function(a , b){
    console.log("Ejecutando la funcion : "+ (a + b));
})(3,4);

console.log(typeof miFuncion);

var  miFuncionTexto = miFuncion.toString();

console.log(miFuncionTexto);

// Funciones flecha 

const sumarFuncionTipoFlecha = (a,b) => a + b;
resultado = sumarFuncionTipoFlecha(3,5);
console.log(resultado);

// Argumentos y parametros 
// Argurmentos valores que pasamos a una funcion
// Parametros son la lista de valores que le pasamos a la funcion


let sumar = function (a = 4,b = 5 ){
    console.log(arguments[0]);
    console.log(arguments[1]);
    console.log(arguments[2]);
    return a+b + arguments[2];
};

resultado = sumar(3,5,7);
console.log(resultado);

// Sumar todos los Argumentos. 


let resultado2 =  sumarTodo(5,3,5,14,6,7);
console.log(resultado2);

function sumarTodo(){
    let sumar = 0;
    for (let i = 0 ; i < arguments.length; i ++){
        sumar += arguments[i]; // sumar = suma + argumentos[i]
    }
    return sumar
}

// Paso por valor y por referencia 

x = 10;

function cambiarValor(a){
    a = 20;
    console.log(a);
}

// Paso por valor
console.log(x);
cambiarValor(x);
console.log(x);
//console.log(a); // No esta definido

// Paso por referencia 

const persona = {
    nombre : "Juan",
    apellido : "Perez"
}

function cambiarValorObjeto(p1){
    p1.nombre = "Carlos";
    p1.apellido = "Lara"
}

console.log(persona);
cambiarValorObjeto(persona);
console.log(persona);

