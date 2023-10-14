let el = (id) => document.getElementById(id);

let image_form = el('image_form'),
    image_wrapper = el('image_wrapper'),
    image_image = el('image_image');

window.onload = () => {
    image_wrapper.style.top = image_form.offsetTop+'px';
    image_wrapper.style.left = image_form.offsetLeft+'px';
    image_image.style.top = image_form.offsetTop+'px';
    image_image.style.left = image_form.offsetLeft+'px';
}
window.onresize = () => {
    image_wrapper.style.top = image_form.offsetTop+'px';
    image_wrapper.style.left = image_form.offsetLeft+'px';   
    image_image.style.top = image_form.offsetTop+'px'; 
    image_image.style.left = image_form.offsetLeft+'px';
}

image_form.onchange = function (evt) {
    let tgt = evt.target;
    let files = tgt.files;
    // FileReader
    if (FileReader && files && files.length) {
        let fr = new FileReader();
        fr.onload = function () {
            image_image.src = fr.result;
            image_image.style.zIndex = 200;
            image_image.style.opacity = 1;
        }
        fr.readAsDataURL(files[0]);
    }
}  