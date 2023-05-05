

class Empleado{
    constructor(nombre, sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    obtenerDetalles(){
        return `Empleado: nombre: ${this.nombre} sueldo: ${this.sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre,sueldo);
        this.departamento = departamento;
    }
    // Polimorfismo
    obtenerDetalles(){
       return `Gerente : ${super.obtenerDetalles()} Departamento: ${this.departamento}`;
    }

}

// Polimorfismo

function imprimir(tipo){
    console.log( tipo.obtenerDetalles() ) ;
    // Palabra intasoft
    if (tipo instanceof Gerente){
        console.log("Es un objeto de tipo Empleado");
        console.log(tipo.departamento);
    }
    else if (tipo instanceof Empleado) {
        console.log("Es un objeto de tipo Gerente");
        console.log(tipo.departamento);
    }
    else if (tipo instanceof Object) {
        console.log("Es un objeto de tipo Objecto");
    }
}

let empleado1 = new Empleado("Carlos", 4000)
console.log( empleado1.obtenerDetalles() )
let gerente1 =  new Gerente("Juan", 5000 , "Sistemas");
console.log( gerente1.obtenerDetalles() );

imprimir(empleado1);
imprimir(gerente1);

// Palabra intasoft



