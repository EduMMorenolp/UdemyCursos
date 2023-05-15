"use strict";
let usuario1 = { nombreUsuario: "Juan", password: "1234", confirmarPassword: "1234" };
console.log(usuario1);
console.log(usuario1.nombreUsuario, usuario1.password);
let avion = {
    abordarTransporte: function () {
        console.log("abordando");
    }
};
avion.abordarTransporte();
