class Persona {
  static contadorPersona = 0;

  constructor(nombre, apellido, edad) {
    this._idPersona = ++Persona.contadorPersona;
    this._nombre = nombre;
    this._apellido = apellido;
    this._edad = edad;
  }
  get idPersona() {
    return this._idPersona;
  }
  get nombre() {
    return this._nombre;
  }
  set nombre(nombre) {
    this._nombre = nombre;
  }
  get apellido() {
    return this._apellido;
  }
  set apellido(apellido) {
    this._apellido = apellido;
  }
  get edad() {
    return this._edad;
  }
  set edad(edad) {
    this._edad = edad;
  }
  toString() {
    return ` ${this._idPersona} ${this._nombre}  
                ${this._apellido} 
                ${this._edad}`;
  }
}

class Empleado extends Persona {
  static contadorEmpleado = 0;

  constructor(nombre, apellido, edad, sueldo) {
    super(nombre, apellido, edad);
    this._idEmpleado = ++Empleado.contadorEmpleado;
    this._sueldo = sueldo;
  }

  get idEmpleado() {
    return this._idEmpleado;
  }

  get sueldo() {
    return this._sueldo;
  }

  set idEmpleado(idEmpleado) {
    this._idEmpleado = idEmpleado;
  }

  set sueldo(sueldo) {
    this._sueldo = sueldo;
  }

  toString() {
    return ` ${super.toString()} ${
      this._idEmpleado
    } ${this._sueldo}`;
  }
}

class Cliente extends Persona {
  static contadorCliente = 0;

  constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this._idCliente = ++Cliente.contadorCliente;
    this._fechaRegistro = fechaRegistro;
  }

  get idCliente() {
    return this._idCliente;
  }

  get fechaRegistro() {
    return this._fechaRegistro;
  }

  set idCliente(idCliente) {
    this._idCliente = idCliente;
  }

  set fechaRegistro(fechaRegistro) {
    this._fechaRegistro = fechaRegistro;
  }

  toString() {
    return (
      " " + super.toString() +
      " " +
      this._idCliente +
      " " +
      this._fechaRegistro
    );
  }
}

// Prueba de la Clase PERSONA

let persona1 = new Persona("Juan", "Perez", 28);

console.log(persona1.toString());

let empleado1 = new Empleado("Pedro", "Sarez", 28, 5000);

console.log(empleado1.toString());

let cliente1 = new Cliente("Clara", "Lara", 35, 1986);

console.log(cliente1.toString());
