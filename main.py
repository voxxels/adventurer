<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Adventure</title>
    <style>
        body { font-family: monospace; background: black; color: lime; }
        #game { white-space: pre-line; height: 300px; overflow-y: auto; border: 1px solid lime; padding: 10px; }
        input { width: 100%; background: black; color: lime; border: 1px solid lime; }
    </style>
</head>
<body>
    <div id="game"></div>
    <input type="text" id="input" placeholder="Type a command...">
    <script>
        const gameDiv = document.getElementById("game");
        const input = document.getElementById("input");
        
        let gameState = "start";
        
        function output(text) {
            gameDiv.innerHTML += text + "<br>";
            gameDiv.scrollTop = gameDiv.scrollHeight;
        }
        
        function processInput(command) {
            command = command.toLowerCase();
            
            if (gameState === "start") {
                if (command.includes("look")) {
                    output("You find yourself in a dark forest. Paths lead north and south.");
                } else if (command.includes("north")) {
                    output("You walk north and find an abandoned cabin.");
                    gameState = "cabin";
                } else if (command.includes("south")) {
                    output("You walk south and fall into a pit. Game over.");
                    gameState = "game over";
                } else {
                    output("Unknown command. Try 'look', 'north', or 'south'.");
                }
            } else if (gameState === "cabin") {
                if (command.includes("enter")) {
                    output("You enter the cabin. It's cozy inside.");
                } else {
                    output("Try exploring more.");
                }
            }
        }
        
        input.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                let command = input.value;
                input.value = "";
                output("> " + command);
                processInput(command);
            }
        });
        
        output("Welcome to the Text Adventure! Type 'look' to begin.");
    </script>
</body>
</html>
