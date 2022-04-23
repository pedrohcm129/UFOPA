function validarUsuario() {
    const userName = document.getElementById("nome")
    const userLastName = document.getElementById("sobrenome")
    const userCpf = document.getElementById("cpf")
    const userEmail = document.getElementById("email")
    const userPhoneNumber = document.getElementById("telefone")
    const userLinkGithub = document.getElementById("linkgithub")

    if (validarLinkGithub(userLinkGithub.value) && validarCpf(userCpf.value) && validarVasio(userName.value, userLastName.value) && validarE_mail(userEmail.value) && validarTelefone(userPhoneNumber.value)) {
        alert("Cadastro realizado!!!")
        window.location.href = "index.html";
    }
}

function validarVasio(variavel) {
    if (variavel === '') {
        return false
    } else {
        return true
    }
}

function validarCpf(cpf = String) {
    let  primeiroVerificador = 0;
    let segundoVerificador = 0;
    if (validarVasio(cpf)) {
        if (cpf.length === 11) {
            for (i = 10; i > 1; i --) {
                primeiroVerificador += parseInt(cpf[10 - i]) * i
            }
            for (i = 11; i > 1; i --) {
                segundoVerificador += parseInt(cpf[11 - i]) * i
            }
            if (primeiroVerificador * 10 % 11 === parseInt(cpf[9]) && segundoVerificador * 10 % 11 === parseInt(cpf[10])) {
                return true
            } else {
                return false
            }
        } else {
            return false
        }
    } else {
        return false
    }
}

function validarE_mail(email) {
    if (validarVasio(email) && email.indexOf('@') > -1) {
        nome = email.substring(0, email.indexOf('@'))
        dominio = email.substring(email.indexOf('@') + 1, email.length)
        if (validarVasio(nome) && validarVasio(dominio)) {
            if (dominio.indexOf('.') > -1) {
                if (validarVasio(dominio.substring(0, dominio.indexOf('.'))) && (validarVasio(dominio.substring(dominio.indexOf('.') + 1, dominio.length)))) {
                    return true
                } else {
                    return false
                }
                } else {
                    return false
                }
            } else {
                return false
            }
    } else {
        return false
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