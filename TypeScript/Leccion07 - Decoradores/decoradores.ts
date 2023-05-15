

function Saludar(target: Function): void{
    target.prototype.Saludar = function():void{
        console.log("Hola Mundo!")
    }

}

@Saludar
class Hola{
    constructor(){}
}

let hola1 = new Hola();
hola1.Saludar();