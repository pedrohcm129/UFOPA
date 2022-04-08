
const button = document.getElementById('butao')
button.addEventListener('click', event => {
    event.preventDefault()
    
    const nome = document.getElementById('nome')
    const sobrenone = document.getElementById('sobrenome')
    const cpf = document.getElementById('cpf')
    const email = document.getElementById('email')
    const telefone = document.getElementById('telefone')
    const linkGithub = document.getElementById('linkgithub')
    
    if (validarLinkGithub(linkGithub.value) && validarCpf(cpf.value) && validarNomeSobrenome(nome.value, sobrenone.value) && validarEmail(email.value) && validarTelefone(telefone.value) && validarLinkGithub(linkGithub.value)) {
        alert("Cadastro realizado!!!")
        window.location.href = "index.html";
    }

})

function validarCpf(strCpf) {
    if (!/[0-9]{1}/.test(strCpf)) {
        alert("CPF inválido!!")
        return false;}
    if (strCpf === "00000000000") {
        alert("CPF inválido!!")
        return false;
    }
    var soma = 0;
    for (var i = 1; i <= 9; i++) {
        soma += parseInt(strCpf.substring(i - 1, i)) * (11 - i);
    }
    var resto = soma % 11;
    if (resto === 10 || resto === 11 || resto < 2) {
        resto = 0;
    } else {
        resto = 11 - resto;
    }
    if (resto !== parseInt(strCpf.substring(9, 10))) {
        alert("CPF inválido!!")
        return false;
    }
    soma = 0;
    for (var i = 1; i <= 10; i++) {
        soma += parseInt(strCpf.substring(i - 1, i)) * (12 - i);
    }
    resto = soma % 11;
    if (resto === 10 || resto === 11 || resto < 2) {
        resto = 0;
    } else {
        resto = 11 - resto;
    }
    if (resto !== parseInt(strCpf.substring(10, 11))) {
        alert("CPF inválido!!")
        return false
    } else {
        return true
    }
}

function validarEmail(email) {
    if (email === '' || email.indexOf('@') == -1) {
        alert("E-mail inválido!!")
        return false
    } else {
        return true
    }
}

function validarNomeSobrenome(nome, sobrenome) {
    if (nome === "" || sobrenome ==="") {
        alert("Nome ou Sobrenome inválido!!")
        return false
    } else {
        return true
    }
}

function validarTelefone(telefone) {
    if (telefone.length === 14 && telefone[0] === '+' && telefone[1] === '5' && telefone[2] === '5') {
        return true
    } else {
        alert("Telefone inválido!!")
        return false
    }
}

function validarLinkGithub(linkGithub) {
    if (linkGithub.indexOf("https://github.com") == -1) {
        alert("Link do GitHub inválido!!")
        return false
    } else {
        return true
    }
}