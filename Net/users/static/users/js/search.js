const d = document;

let el = (id) => d.getElementById(id);

let form = el('form_search'),
    input_search = el('id_name'),
    names = d.getElementsByTagName('p');

let profile = (e) => {
    let t = e.target.innerHTML;
    input_search.value = t;
    form.submit();
}   
