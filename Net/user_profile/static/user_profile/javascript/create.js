const d = document;

let el = (id) => d.getElementById(id)

let button = el('button'),
    form = el('form'),
    user_get = el('user'),
    slug = el('slug_field');

button.onclick = () => {
    slug.value = user_get.innerText;
    console.log('Слаг для пользователя добавлен');
    form.submit();
}