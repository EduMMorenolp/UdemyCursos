


let suma = function (a:number, b:number){
    return a+ b;
}

console.log(suma(5,3));

let sumaFlecha = (a:number, b:number) => a + b;

let sumaFlecha2 = (a:number, b:number) => {
    return a+ b;
}

console.log(sumaFlecha(2,2));
console.log(sumaFlecha2(5,2));

var obtebernombre = function(){
    return "Juan Perez";
}

console.log(obtebernombre());

let obtebernombre2 = () => "juan perezito";

console.log(obtebernombre2());