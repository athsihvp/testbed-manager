async function loadImages() {
    let res = await fetch("/api/images");
    let data = await res.json();

    let select = document.getElementById("imageSelect");

    data.images.forEach(img => {
        let option = document.createElement("option");
        option.value = img.name;
        option.text = img.name;
        select.appendChild(option);
    });
}

async function submitRequest() {

    let image = document.getElementById("imageSelect").value;

    let blades = [];

    document.querySelectorAll("input[type=checkbox]").forEach(cb => {
        if (cb.checked) blades.push(cb.value);
    });

    let res = await fetch("/api/provision", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({image, blades})
    });

    let data = await res.json();

    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}

loadImages();