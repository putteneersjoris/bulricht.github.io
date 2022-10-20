imageUrls.forEach(element => {
    createDiv(element);
});

function createDiv(text) {
    let img = document.createElement("img")
    img.classList.add('images')
    img.src = text
    document.getElementById("images").appendChild(img);
    return img;
}
