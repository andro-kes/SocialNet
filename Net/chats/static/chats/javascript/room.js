const roomName = JSON.parse(document.getElementById('room-name').textContent);

const user = document.getElementById('user'),
    div = document.getElementById('wrapper');

const chatSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

window.onload = () => {
    div.scrollTop = div.scrollHeight;
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    let m = '';
    if(user.innerHTML == data.user){
        m = '<p class="you"><text class="you-message">'+data.message+'</text></p>';
    } else{
        m = '<p class="friend"><text class="friend-message">'+data.message+'</text></p>';
    }
    document.querySelector('#chat-log').innerHTML += m;
    div.scrollTop = div.scrollHeight;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    if(document.querySelector('#chat-message-input').value){
        chatSocket.send(JSON.stringify({
            'message': message,
            'user': user.innerHTML,
        }));
    }
    messageInputDom.value = '';
};