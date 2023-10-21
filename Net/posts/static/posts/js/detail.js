const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
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
                <p class'message'>${m}</p>
            </div>
            <div class='date'>
                <p class='date-data'>${date.date}.${date.month + 1}.${date.year}</p>
                <p class='date-data'>${date.hours}:${date.minutes}:${date.seconds}</p>
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
            'time': {
                'year': date.getFullYear(),
                'month': date.getMonth(),
                'date': date.getDate(),
                'hours': date.getHours(),
                'minutes': date.getMinutes(),
                'seconds': date.getSeconds(),
            }
        }));
    }
    messageInputDom.value = '';
};