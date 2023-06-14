
import { Persona } from "./persona.model";


export class PersonaServicio{

    personas: Persona[] = [
        new Persona("Juan", "Perez"),
        new Persona("Laura", "Juarez"),
        new Persona("Karla", "Lara")
       ];

       personaAgregada(persona: Persona){
        this.personas.push(persona);
        }

}