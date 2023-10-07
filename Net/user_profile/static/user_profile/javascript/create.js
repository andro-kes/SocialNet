const d = document;

let el = (id) => d.getElementById(id),
    getcl = (cl_name) => d.getElementsByClassName(cl_name);

let button = el('button'),
    form = el('form'),
    user_get = el('user'),
    slug = el('slug_field');

let ava = d.getElementsByClassName('ava'),
    ava_form = d.getElementsByClassName('ava-link'),
    ava_image = d.getElementsByClassName('ava-image'),
    ava_div = d.getElementsByClassName('ava-div'),
    ava_clear = el('ava-clear_id'),
    delete_ava = d.getElementsByClassName('delete-ava');

let forms = {
    'name_forms': getcl('name_form'),
    'bio_forms': getcl('bio_form'),
    'surnames_forms': getcl('surname_form'),
    'status_forms': getcl('status_form'),
}

button.onclick = () => {
    for(let form in forms){
        if(forms[form][0].value){
            forms[form][1].value = forms[form][0].value;
        } else{
            forms[form][0].value = forms[form][1].value;
        } 
    }
    slug.value = user_get.innerText;
    form.submit();
}

window.onload = () => {
    ava[0].style.top = ava_form[0].offsetTop+'px';
    ava[1].style.top = ava_form[1].offsetTop+'px';
    ava_div[0].style.top = ava_form[0].offsetTop+'px';
    ava_div[1].style.top = ava_form[1].offsetTop+'px';
}
window.onresize = () => {
    ava[0].style.top = ava_form[0].offsetTop+'px';
    ava[1].style.top = ava_form[1].offsetTop+'px';
    ava_div[0].style.top = ava_form[0].offsetTop+'px';
    ava_div[1].style.top = ava_form[1].offsetTop+'px';
}


// вставка картинки
for(input of ava_form){
    input.onchange = function (evt) {
        console.log('work')
        if(!f){
            clear_ava.checked = false;
            buttons[0].style.display = 'block';
            buttons[1].style.display = 'block';
        }
        let tgt = evt.target;
        let files = tgt.files;
        if(ava_form[0].files.length){
            ava_form[1].files = ava_form[0].files;
        } else{
            ava_form[0].files = ava_form[1].files
        }
        // FileReader
        if (FileReader && files && files.length) {
            let fr = new FileReader();
            fr.onload = function () {
                ava_image[0].src = fr.result;
                ava_div[0].style.display = 'block';
                ava_image[1].src = fr.result;
                ava_div[1].style.display = 'block';
            }
            fr.readAsDataURL(files[0]);
        }
    }  
}

if(!(ava_clear)){
    for(button of delete_ava){
        button.style.display = 'none';
    }
}