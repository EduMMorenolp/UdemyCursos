

// PROMESAS

let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = true;
    if (expresion){
        resolver("Resuelto");
    }else{
        rechazar("RECHAZADO !");
    }
});


miPromesa.then(
    valor => console.log(valor),
    error => console.log(error)
);


miPromesa
    .then( valor => console.log(valor + " 2 "))
    .catch(error => console.log(error));

// setTimeout + Promesas


let miPromesa2 = new Promise((resolver) => {
    console.log("Al Principio");
    setTimeout( () => resolver("Saludos con setTimeout + Promesa"), 2000)
    console.log("Fin Promesa setTimeout ");
}
); 

miPromesa2.then(
    valor => console.log(valor)
);

// Async + Promesas 
// indica que una funcion regresa una promesa

async function miFuncionConPromesa(){
    return "Saludos con Async + Promesa"
}

miFuncionConPromesa().then( valor => console.log(valor) );

// Await + Async 

async function miFuncionConPromesaYAwait(){
    let miPromesa = new Promise( resolver => {
        resolver("Promesa con await");
    })
    // await solo se puede usar dentro de una funcion async
    console.log( await miPromesa);
}

miFuncionConPromesaYAwait();

// Todo Juntos

async function miFuncionConPromesaYAwaitYTimeout(){
    console.log("Al Principio Funcion");
    let miPromesa =  new Promise(resolver => (
        setTimeout(() => resolver("Promesa con todo .... "), 10000)
    ));
    console.log( await miPromesa);
    console.log("Fin Funcion con todo..");
}

miFuncionConPromesaYAwaitYTimeout();

