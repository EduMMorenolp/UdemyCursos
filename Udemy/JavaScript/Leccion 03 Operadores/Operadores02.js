//Ejemplo AND (&&), regresa true solo si ambos operandos son true
let a = 15;
let valMin = 0,
  valMax = 10;

if (a >= valMin && a <= valMax) {
  console.log("Dentro de rango");
} else {
  console.log("Fuera de rango");
}

//Ejemplo OR (||), regresa true si cualquier operando es true
let vacaciones = false,
  diaDescanso = true;
if (vacaciones || diaDescanso) {
  console.log("Padre puede asistir al juego del hijo");
} else {
  console.log("El padre está ocupado");
}

//Operador Ternario, elije entre las 2 opciones sea falso o verdadero.
let resultado = 1 > 2 ? "verdadero" : "falso";
console.log(resultado);
let resultado2 = 11 > 2 ? "verdadero" : "falso";
console.log(resultado2);

let numero = 110;
resultado = numero % 2 == 0 ? "Número par" : "Número impar";
console.log(resultado);

// Convertir String a Numero (int)

let miNumero = "17";
console.log(typeof miNumero);

let edad = Number(miNumero);
console.log(typeof edad);
if (edad >= 18) {
  console.log("Puede votar");
} else {
  console.log("Muy joven para votar");
}

//Forma abreviada del if con el Operador ?
let resultado4 = edad >= 17 ? "Puede votar" : "Muy joven para votar";
console.log(resultado4);

// Funcion isNaN ( Si no es, entonces... )

edad = "a"
// Si no es un numero entonces.. 
if (isNaN(edad)){
    console.log("No es un numero");
}else{
    let resultado4 = edad >= 17 ? "Puede votar" : "Muy joven para votar";
    console.log(resultado4);
}
