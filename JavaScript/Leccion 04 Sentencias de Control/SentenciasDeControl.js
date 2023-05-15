


let condicion = true;

// CONDICION IF ELSE ( si, sino )

if (condicion){
    console.log("condicion verdadera");
}
else{
    console.log("condicion falsa");
}

let numero = 6;

if (numero == 1){
    console.log("numero uno");
}else if (numero == 2){
    console.log("numero dos");
}else if (numero == 3){
    console.log("numero tres")
}else if (numero == 4){
    console.log ("numero cuatro")
}else{
    console.log("Numero desconocido")
}

// ESTACIONES DEL AÑO

let mes =4;
let estacion;

if( mes == 1 || mes == 2 || mes == 12){
    estacion = "Invierno";
}
else if( mes == 3 || mes == 4 || mes == 5){
    estacion = "Primavera";
}
else if( mes == 6 || mes == 7 || mes == 8 ){
    estacion = "Verano";
}
else if( mes == 9 || mes == 10 || mes == 11 ){
    estacion = "Otoño";
}
else{
    estacion = "Valor incorrecto";
}
console.log(estacion);

// SENTENCIA DE "SEGUN" ( Switch )


let numeros = 2;
let numeroTexto = "valor desconocido";
switch (numeros){
    case 1:
        numeroTexto = "numero uno";
        break
    case 2:
        numeroTexto = "numero dos";
        break
    case 3:
        numeroTexto = "numero tres";
        break
    default:
        numeroTexto = "caso no encontrado";
}
console.log(numeroTexto);

let meses = 6;
let estaciones = 'Estación desconocida';

switch( meses ){
    case 1: case 2: case 12:
        estaciones = 'Invierno';
        break;
    case 3: case 4: case 5:
        estaciones = 'Primavera';
        break;
    case 6: case 7: case 8:
        estaciones = 'Verano';
        break;
    case 9: case 10: case 11:
        estaciones = 'Otoño';
        break;
    default:
        estaciones = 'Valor incorrecto';                
}
console.log(estaciones);

