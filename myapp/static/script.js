const clientId = Math.random().toString(36).substring(2, 15);
const socket = new WebSocket(`ws://${window.location.host}/ws/${clientId}`);

socket.onmessage = function(event) {
    const messagesList = document.getElementById("messagesList");
    const li = document.createElement("li");
    li.textContent = event.data;
    messagesList.appendChild(li);
};

function sendMessage() {
    const input = document.getElementById("messageInput");
    socket.send(input.value);
    input.value = '';
}

function return_django() {
    window.location.href = "http://localhost:8000/home";
}

