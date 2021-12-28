const trashContainer = document.querySelector('.trash-container')
const nameElement = document.querySelector('.name')
var icon = ""
setupTrash()
function setupTrash() {
    for (let i = 0; i < 50; i++) {
        num = randomNumberBetween(0,100)
        if(num < 15) {
            icon = "bag"
        } else if ( num < 30 ) {
            icon = "bottle"
        } else if ( num < 45 ) {
            icon = "headphones"
        } else if (num < 60 ) {
            icon = "phone";
        } else if ( num < 75 ) {
            icon = "takeout"
        } else if ( num < 90 ) {
            icon = "toy-car"
        }
        createTrash(icon);
    }
}
function createTrash(icon) {
    const img = document.createElement("img")
    const top = randomNumberBetween(0, 50)
    const size = top / 5 + 1
    img.classList.add("trash")
    img.src = `imgs/${icon}.svg`
    img.style.width = `${size}vmin`
    img.style.height = `${size}vmin`
    img.style.top = `${top}vh`
    img.style.left = `${randomNumberBetween(0, 100)}vw`
    img.style.setProperty("--rotation", `${randomNumberBetween(-30, 30)}deg`)
    trashContainer.appendChild(img)
}

function randomNumberBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1))
}
