

class Empleado extends Persona{

    static contadorEmpleado = 0;

    constructor(sueldo){
        this._idEmpleado = ++Persona.contadorPersona;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get sueldo(){
        return this._sueldo;
    }

    set sueldo(sueldo){
        this._sueldo = sueldo;
    }

    toString(){
        return (`Persona : ${super.toString()} ID Empleado : ${this._idEmpleado}Sueldo : ${this._sueldo}`);
    }
}