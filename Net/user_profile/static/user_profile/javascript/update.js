let cl = (cl_name) => d.getElementsByClassName(cl_name);
let rm = (elem) => {
    if(['TEXTAREA', 'INPUT', 'DIV', 'H1'].includes(elem.tagName))
        return false;
    return true;
}

let infa = cl('bio-ava')[0],
    infa_phone = cl('name-surname-status')[1],
    rm_childs = [],
    rm_childs_ph = [];

let buttons = cl('delete-ava'),
    clear_ava = el('ava-clear_id');

let f = true;

for(let el of infa.childNodes){
    if(rm(el)){
        rm_childs.push(el);
    }
}
for(let el of infa_phone.childNodes){
    if(rm(el)){
        rm_childs_ph.push(el);
    }
}
for(child of rm_childs){
    infa.removeChild(child);
}
for(child of rm_childs_ph){
    infa_phone.removeChild(child);
}

for(button of buttons){
    button.onclick = () => {
        console.log(clear_ava.checked)
        if(!clear_ava.checked){
            clear_ava.checked = true;
            ava_image[0].src = '/static/user_profile/img/no_ava.jpg';
            ava_image[1].src = '/static/user_profile/img/no_ava.jpg';
            buttons[0].style.display = 'none';
            buttons[1].style.display = 'none';
            f = false;
        }
    }
}