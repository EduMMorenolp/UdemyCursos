


"use strict";

try{
    var x = 10;
    //miFuncion();
    throw "Mi error";
}
catch(error){
    console.log(error);
}
finally{
    console.log("Terminando la correccion de Errores");
}


console.log("Continuamos...");


let resultado = "";

try{
    if ( isNaN(resultado)) throw " No es un numero ";
    else if ( resultado === "") throw " Es una Cadena Vacia ";
    else if ( resultado >= 0) throw " Valor positivo ";
    else if ( resultado < 0) throw " Valor negativo ";
}
catch(error){
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally{
    console.log("Terminando la correccion de Errores");
}