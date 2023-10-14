const d = document;

let el = (id) => d.getElementById(id);

let posts = el('posts'),
    posts_wrapper = el('posts_wrapper'),
    close = el('close');

let header = d.getElementsByTagName('header')[0];

posts.onclick = () => {
    posts_wrapper.style.display = 'flex';
    header.style.display = 'none';
}

close.onclick = () => {
    posts_wrapper.style.display = 'none';
    header.style.display = 'flex';
}