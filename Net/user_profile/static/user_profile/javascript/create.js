const d = document;

let el = (id) => d.getElementById(id)

let button = el('button'),
    form = el('form'),
    user_get = el('user'),
    slug = el('slug_field');

let ava = d.getElementsByClassName('ava'),
    ava_form = d.getElementsByClassName('ava-link');

button.onclick = () => {
    slug.value = user_get.innerText;
    console.log('Слаг для пользователя добавлен');
    form.submit();
}

window.onload = () => {
    ava[0].style.top = ava_form[0].offsetTop+'px';
    ava[1].style.top = ava_form[1].offsetTop+'px';
}
window.onresize = () => {
    ava[0].style.top = ava_form[0].offsetTop+'px';
    ava[1].style.top = ava_form[1].offsetTop+'px';
}