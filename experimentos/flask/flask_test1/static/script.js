
fetch("./api").then(async(response) => {
    const json = await response.json();
    document.querySelector("#name").textContent = json.name;
    document.querySelector("#date").textContent = json.date;
});



fetch("./api/hw").then(async(response) => {
    const json = await response.json();
    document.querySelector("#arquitectura").textContent = json.arquitectura;
    document.querySelector("#cpu_cores").textContent = json.cpu_cores;
    document.querySelector("#nombre_maquina").textContent = json.nombre_maquina;
    document.querySelector("#procesador").textContent = json.procesador;
    document.querySelector("#sistema_operativo").textContent = json.sistema_operativo;
    document.querySelector("#version_os").textContent = json.version_os;
});

