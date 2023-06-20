
import { Injectable } from "@angular/core";
import { LogginService } from "./LogginService.service";
import { Persona } from "./persona.model";

@Injectable()
export class PersonaServicio{

    personas: Persona[] = [
        new Persona("Juan", "Perez"),
        new Persona("Laura", "Juarez"),
        new Persona("Karla", "Lara")
       ];

       constructor(private logginService: LogginService){}

       personaAgregada(persona: Persona){

        this.logginService.enviaMensajeConsola(" agregamos Persona :" + persona.nombre);
        this.personas.push(persona);
        }

}