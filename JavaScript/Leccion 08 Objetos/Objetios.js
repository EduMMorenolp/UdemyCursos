

// Objetos 

let x = 10;
console.log(x.length);

let persona = {
    nombre : "Juan",
    apellido : "Perez",
    email : "jperes@gamil.com",
    edad : 28,
    idioma : "es",
    nombreCompleto : function(){
        return this.nombre + " " + this.apellido; 
    },
    get nombreGetCompleto(){        
        return (this.nombre + " " + this.apellido); 
    },
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang( lang ){
        this.idioma =  lang.toUpperCase();
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona);

// Agregar Metodos a Objetos 

console.log(persona.nombreCompleto());

// Creacion de Objetos 

let persona2 = new Object();

persona2.nombre = "Carlos";
persona2.apellido = "Maimi";
persona2.direccion = "Saturno 15";

console.log(persona2);

// Acceder a propiedades de Objetos 

console.log(persona["apellido"]);

// for in

for ( nombrePropiedad in persona){
    console.log( nombrePropiedad );
    console.log( persona[nombrePropiedad]);    
}

// Agregar porpiedad al objeto 

persona.edad = 31;
console.log(persona);

// Elimar propiedad

delete persona.edad;

console.log(persona);

// Imprimir un Objeto

// Por valor de cada propiedad

console.log(persona.nombre + ", " + persona.apellido);

//for in 

let personaArray =  Object.values(persona);
console.log(personaArray);

let personaString = JSON.stringify(persona);

console.log(personaString);

//  Metodo Get en Objetos (Obtener)

console.log( persona.nombreGetCompleto ); 

// Metodo Set en Obejetos (Cambiar)

console.log( persona.lang );

persona.lang = "es_arg"

console.log( persona.lang );