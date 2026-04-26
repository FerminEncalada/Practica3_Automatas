const API="http://127.0.0.1:5000";

const datos={

"afd/transacciones":{
alfabeto:"A, C, L",
ejemplo:"Ej: ACL",
descripcion:
"Valida la secuencia Autorización → Captura → Liquidación.",

transiciones:
`q0 --A--> q1
q1 --C--> q2
q2 --L--> qf`,

imagen:"img/transacciones.png"
},

"afd/handshake":{
alfabeto:"S, Y, A",
ejemplo:"Ej: SYA",
descripcion:
"Simulación del protocolo TCP Three-Way Handshake.",

transiciones:
`q0 --S--> q1
q1 --Y--> q2
q2 --A--> qf`,

imagen:"img/handshake.png"
},

"afd/cerradura":{
alfabeto:"F, O",
ejemplo:"Ej: FFO",
descripcion:
"Cerradura que se bloquea tras tres fallos.",

transiciones:
`q0 --F--> q1
q1 --F--> q2
q2 --F--> Bloqueado
(O abre)`,

imagen:"img/cerradura.png"
},

"afnd/genetica":{
alfabeto:"K, G, X, F",
ejemplo:"Ej: KGXXF",
descripcion:
"Reconoce el patrón K G X* F.",

transiciones:
`q0 --K-→q1
q1 --G-→q2
q2 --X-→q2
q2 --F-→qf`,

imagen:"img/genetica.png"
},

"afnd/usuario":{
alfabeto:"H, S, C",
ejemplo:"Ej: HSSC",
descripcion:
"Reconoce HOME SEARCH+ CART.",

transiciones:
`q0 --H-→q1
q1 --S-→q2
q2 --S-→q2
q2 --C-→qf`,

imagen:"img/usuario.png"
},

"afnd/telemetria":{
alfabeto:"H, T, U, C",
ejemplo:"Ej: HTUC",
descripcion:
"Valida HDR (TEMP|HUM)* CRC.",

transiciones:
`q0 --H-→q1
q1 --T/U-→q1
q1 --C-→qf`,

imagen:"img/telemetria.png"
}

};



function actualizarInfo(){

const tipo=
document.getElementById("tipo").value;

let d=datos[tipo];

document.getElementById("alfabeto").innerText=
d.alfabeto;

document.getElementById("descripcion").innerText=
d.descripcion;

document.getElementById("transiciones").innerText=
d.transiciones;

document.getElementById("diagrama").src=
d.imagen;

document.getElementById("cadena").placeholder=
d.ejemplo;

document.getElementById("resultado").innerText=
"Esperando ejecución...";
}


function evaluar(){

const tipo=
document.getElementById("tipo").value;

const cadena=
document.getElementById("cadena").value;

fetch(`${API}/${tipo}`,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({cadena})
})
.then(r=>r.json())
.then(data=>{

const r=
document.getElementById("resultado");

if(data.valido){
r.innerText="✅ Cadena Aceptada";
r.className="valido";
}
else{
r.innerText="❌ Cadena Rechazada";
r.className="invalido";
}

})

}


actualizarInfo();