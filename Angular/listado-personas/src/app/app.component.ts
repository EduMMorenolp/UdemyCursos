import { Component, OnInit } from '@angular/core';
import { Persona } from './persona.model';
import { PersonaServicio } from './Persona.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  

  titulo:string = 'Listado de Personas';
  
  personas: Persona[] = [
    // Ahora lo Inician en Persona.service
   //new Persona("Juan", "Perez"),
   //new Persona("Laura", "Juarez"),
   //new Persona("Karla", "Lara")
  ];

  constructor ( private personaService: PersonaServicio){}

  ngOnInit(): void {
    this.personas = this.personaService.personas;
  }

  //personaAgregada(persona: Persona){
  //this.personas.push(persona);
  //  this.personaService.personaAgregada(persona);
  //}

}