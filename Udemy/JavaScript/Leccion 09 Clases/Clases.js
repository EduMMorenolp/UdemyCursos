

class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
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
        return this._nombre + " " + this._apellido;
    }
    toString(){
        // Polimorfismo ( multiples formas en tiempo de ejecucion)
        // Depende de tipo padre o tipo hijo
        return this.nombreCompleto();
    }
}

// En las CLASES NO SE APLICA HOSTING (primero se tiene que crear la clase antes de usarla)

let persona1 = new Persona("Juan","Perez");

console.log(persona1);

let persona2 = new Persona("Calos","Lara");

console.log(persona2);

// Metodo Get y Set
console.log( persona1.nombre );
persona1.nombre = "Juan Carlos";
console.log( persona1.nombre );

// Herencia de clases

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
}

let empleado1 = new Empleado("Maria","Gimenes","Sistemas");

console.log(empleado1);
console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

// clase Object - ToString - Polimorfismo

console.log(empleado1.toString())
console.log(persona1.toString());

