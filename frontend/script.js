const API = "http://127.0.0.1:5000"; // backend Flask

const datos = {
    "afd/transacciones": {
        alfabeto: "{A, C, L}",
        transiciones: "q0-A→q1\nq1-C→q2\nq2-L→qf",
        imagen: "img/transacciones.png"
    },
    "afd/handshake": {
        alfabeto: "{S, Y, A}",
        transiciones: "q0-S→q1\nq1-Y→q2\nq2-A→qf",
        imagen: "img/handshake.png"
    },
    "afd/cerradura": {
        alfabeto: "{F, O}",
        transiciones: "q0-F→q1\nq1-F→q2\nq2-F→bloqueado",
        imagen: "img/cerradura.png"
    },
    "afnd/genetica": {
        alfabeto: "{K, G, X, F}",
        transiciones: "q0-K→q1\nq1-G→q2\nq2-X→q2\nq2-F→qf",
        imagen: "img/genetica.png"
    },
    "afnd/usuario": {
        alfabeto: "{H, S, C}",
        transiciones: "q0-H→q1\nq1-S→q2\nq2-S→q2\nq2-C→qf",
        imagen: "img/usuario.png"
    },
    "afnd/telemetria": {
        alfabeto: "{H, T, U, C}",
        transiciones: "q0-H→q1\nq1-T/U→q1\nq1-C→qf",
        imagen: "img/telemetria.png"
    }
};

function evaluar() {
    const tipo = document.getElementById("tipo").value;
    const cadena = document.getElementById("cadena").value;

    fetch(`${API}/${tipo}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ cadena })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("resultado").innerText =
            data.valido ? "✅ Cadena válida" : "❌ Cadena inválida";
    });

    document.getElementById("alfabeto").innerText = datos[tipo].alfabeto;
    document.getElementById("transiciones").innerText = datos[tipo].transiciones;
    document.getElementById("diagrama").src = datos[tipo].imagen;
}