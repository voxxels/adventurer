const gameOutput = document.getElementById("gameOutput");
const userInput = document.getElementById("userInput");

function handleInput() {
    let command = userInput.value.toLowerCase();
    userInput.value = "";  // Clear input box

    if (command.includes("look")) {
        gameOutput.innerHTML += "<p>You see a dark forest ahead...</p>";
    } else if (command.includes("walk")) {
        gameOutput.innerHTML += "<p>You walk forward cautiously...</p>";
    } else {
        gameOutput.innerHTML += "<p>Invalid command.</p>";
    }
}
