import { Component, ViewChild, ElementRef } from '@angular/core';
import { Persona } from '../persona.model';
import { LogginService } from '../LogginService.service';
import { PersonaServicio } from '../Persona.service';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
  providers: [LogginService]

})
export class FormularioComponent {

  //@Output() personaCreada = new EventEmitter<Persona>();

  //nombreInput:string = "";
  //apellidoInput:string ="";

  //ViewChild
  @ViewChild("nombreInput") nombreInput: ElementRef;
  @ViewChild("apellidoInput") apellidoInput: ElementRef;

  constructor(private logginService:LogginService,
              private PersonaServicio: PersonaServicio) {

  }

//agregarPersona(nombreInput:HTMLInputElement, apellidoInput:HTMLInputElement){
  agregarPersona(){
    let persona1 = new Persona( this.nombreInput.nativeElement.value ,
       this.apellidoInput.nativeElement.value );
    //this.personaCreada.emit(persona1);
    this.PersonaServicio.personaAgregada(persona1);
    //this.logginService.enviaMensajeConsola("Enviamos persona nombre : " + persona1.nombre + " apellido : " + persona1.apellido)

  }
}
