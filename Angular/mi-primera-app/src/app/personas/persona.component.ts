import { Component } from "@angular/core";


@Component({
    selector: "app-personas",
    templateUrl: "./persona.component.html",
    styleUrls: ["./persona.component.css"] 
    //styles:["h1{color: red}"]
})

export class PersonasComponent{

    deshabilitar = false;
    mensaje = "No se agregado ninguna persona";
    titulo = "Licenciado";
    mostrar = false;

    agregarPersona(){
        this.mostrar = true;
        this.mensaje = "Persona Agregada";
    }



    //modificarTitulo(event: Event){
      //  this.titulo = (<HTMLInputElement>event.target).value; 
    // }
    
}