let a = 3, b = 2;
let z = a + b;
console.log("Resultado de la suma: " + z );

z = a - b;
console.log("Resultado de la resta: " + z);

z = a * b;
console.log( "Resultado de la mult: " + z);

z = a / b;
console.log( "Resultado de la division: " + z);

z = a % b;//residuo de la division
console.log( "Resultado de operacion modulo (residuo):" + z);

z = a ** b;
console.log( "Resultado de operador exponente:" + z);

//Incremento
//Pre-incremento (el operador ++ antes de la variable)
z = ++a;
console.log(a);
console.log(z);

//Post-incremento (el operador ++ despues de la variable)
z = b++;
console.log(b);
console.log(z);

//Decremento
//Predecremento
z = --a;
console.log(a);
console.log(z);

//Postdecremento
z = b--;
console.log(b);
console.log(z);

/*
Prioridades de OPERACIONES (imagen png)
*/

a = 3, b = 2, c = 1;
let d = 4;

z = a * b + c / d;
console.log(z);

z = c + a * b / d;
console.log( z ); 

z = (c + a) * b / c;
console.log(z);

//OPERADOR DE ASIGNACION 

a = 1;
a += 3; // a = a + 3
console.log(a);
a -= 2; // a = a - 2
console.log(a);

/*

*= Multiplicacion
/= Division
%= Modeulo
**= Potencia

*/

//OPERADORES DE COMPARACION

a = 3, b = 2, c = 3;
z = a == c; // se revisa el valor sin importar el tipo
console.log(z)
z = a != c; // se revisa el valor sin importar el tipo
console.log(z);
z = a === c;// revisa los valores pero tambien los tipos
console.log(z);
z = a !== c;// revisa los valores pero tambien los tipos
console.log(z);

z = a < b; // A menor que B
console.log(z);
z = a <= b; // A menor o igual que B
console.log(z);
z = a > b;  // A mayor que B
console.log(z);
z = a >= b; // A matoy o igual que B
console.log(z);


