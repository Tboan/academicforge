/**
 * Created by will on 3/19/16.
 */

function is_name_valid(){
    var name = document.getElementById('name');
    var error = document.getElementById('error-name');

    if(name.value.length > 0) {
        error.innerHTML = '';
        return true;
    }
    else {
        error.innerHTML = 'Campo de nome não pode estar vazio!';
        return false;
    }
}

