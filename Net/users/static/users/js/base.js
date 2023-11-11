const doc = document;

let elem = (id) => doc.getElementById(id);

let b = elem('menu_button'),
    menu = elem('hide_menu'),
    close_menu = elem('close');

b.onclick = () => {
    menu.style.display = 'flex';
}
close_menu.onclick = () => {
    menu.style.display = 'none';
}
doc.getElementsByTagName('body')[0].onresize = () => {
    menu.style.display = 'none';
}