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

