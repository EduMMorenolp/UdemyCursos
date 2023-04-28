

// CICLOS Mientras (While)

let contador = 0;

while(contador < 3 ){
    contador++;
    console.log(contador);
}
console.log("Fin ciclo while");

// Ciclos Hacer Mientras (DO WHILE)
// Se ejecuta almenos 1 vez
 
contador = 0;

do{
    console.log(contador);
    contador++;
}while(contador < 3);
console.log("Fin ciclo do while")

// CICLOS Para (for) 

contador = 0;

for (contador = 0 ; contador < 3; contador++){
    console.log(contador);
}
console.log("Fin ciclo for");

// Palabra Break (terminar)

for (contador = 0 ; contador < 10; contador++){
    if (contador % 2 == 0){
        console.log(contador);
    }else{
        console.log(contador);
        break;
    }
}
console.log("Fin ciclo for");

// Palabra Continue (Continuar)

for (contador = 0 ; contador < 10; contador++){
    if (contador % 2 !== 0){
        continue; // ir a la siguiente iteracion
        console.log(contador);
    }else{
        console.log(contador);
    }
}
console.log("Fin ciclo for");

// Etiquetas (Go to) // NO RECOMENDABLE USAR. 

inicio:
for (contador = 0 ; contador < 10; contador++){
    if (contador % 2 !== 0){
        continue inicio; 
    }
    console.log(contador);
} 