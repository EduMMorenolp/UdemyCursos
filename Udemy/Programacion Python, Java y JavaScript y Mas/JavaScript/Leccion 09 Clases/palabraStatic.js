


class Persona{



    static contadorObjetosPersona = 0; // atributo de clase

    static get MAX_OBJ(){
        return 3;
    }

    email = "Valor default email"; // atributos de nuestros objetos 


 
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        //Persona.contadorObjetosPersona++;
        if (Persona.contadorObjetosPersona < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorObjetosPersona;
        }
        else{
            console.log("Limite de Objetos Creados");
        }
        }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return  this.idPersona + ": " + this._nombre + " " + this._apellido;
    }
    toString(){
        // Polimorfismo ( multiples formas en tiempo de ejecucion)
        // Depende de tipo padre o tipo hijo
        return this.nombreCompleto();
    }
    static saludar(){
        console.log("saludar desde static")
    }
    static saludar2(persona){
        console.log(persona.nombre);
    }
}

class Empleado extends Persona{ 
    
    constructor(nombre, apellido,departamento){
        super(nombre, apellido);
        this._departamento =  departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //SobreEscritura
    nombreCompleto(){
        return super.nombreCompleto() + ", " + this._departamento
    }
    // Sobreescribiendo el metodo de la clase Padre (Object)
    toString(){
        // Polimorfismo ( multiples formas en tiempo de ejecucion)
        // Depende de tipo padre o tipo hijo
        return this.nombreCompleto();
    }
    static saludar(){
        console.log("saludar desde static")
    }
}

let persona1 = new Persona("Juan","Perez");
let empleado1 = new Empleado("Carlos", "Perez", "Sistemas")

// No es posible llamar un metodo static desde un objeto

//persona1.saludar();

Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(persona1);

console.log(persona1.contadorObjetosPersona);
// Solo se puede llamar desde la clase y no desde objetos.
console.log(Persona.contadorObjetosPersona);
// Las clases hijas tmb heredan los staticos
console.log(Empleado.contadorObjetosPersona);

// Atributos Staticos y No Staticos

console.log( persona1.email );
console.log( empleado1.email );
console.log( Persona.email );
console.log( Empleado.email );

// Ejemplo de uso de la Palabra Static

console.log( persona1.toString());
console.log( empleado1.toString());

// Variable Statica solo lectura


console.log(Persona.MAX_OBJ);

let persona3 = new Persona("Juan Carlos","Perez");
let persona4 = new Persona("Sancho","Panza");

console.log( persona3.toString());
console.log( persona4.toString());