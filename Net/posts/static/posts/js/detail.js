const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/post/'
    + roomName
    + '/'
);

let comments_chat = document.querySelector('.field-comments');
window.onload = () => {
    comments_chat.scrollTop = comments_chat.scrollHeight;
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data)
    let m = data.message;
    let user = data.user;
    let date = data.time;
    let message = `
        <div class='message'>
            <div class='user-m'>
                <p class='user'>${user}</p>
                <p class'='message-text'>${m}</p>
            </div>
            <div class='date'>
                <p class='date-data'>${date.month} ${date.year} г. ${date.hours}:${date.minutes}</p>
            </div>
        </div>
    `;
    document.querySelector('.field-comments').innerHTML += message;
    comments_chat.scrollTop = comments_chat.scrollHeight;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('.input-send').focus();
document.querySelector('.input-send').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('.button-send-message').click();
    }
};

document.querySelector('.button-send-message').onclick = function(e) {
    const messageInputDom = document.querySelector('.input-send');
    const message = messageInputDom.value;
    const date = new Date();
    if(document.querySelector('.input-send').value){
        chatSocket.send(JSON.stringify({
            'message': message,
            'user': document.getElementById('user').innerHTML,
            'post_id': document.getElementById('post_id').innerHTML,
            'time': {
                'year': date.getFullYear(),
                'month': date.toLocaleString('default', { month: 'long', day: 'numeric' }),
                'hours': date.getHours(),
                'minutes': date.getMinutes(),
            }
        }));
    }
    messageInputDom.value = '';
};