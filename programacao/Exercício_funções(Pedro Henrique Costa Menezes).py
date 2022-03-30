#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def soma(a):
    r = 2 * a
    print(f'{a} x {"2"} = {r}')


soma(int(input(f'valor: ')))


# In[ ]:


#2
from math import pi


def compcir(raio):
    return raio * pi * 2


print(compcir(int(input('Digite o raio: '))))


# In[ ]:


#3
def soma(a, b):
    r = a + b
    return r


def subtracao(a, b):
    r = a - b
    return r


def multiplicacao(a, b):
    r = a * b
    return r


def divisao(a, b):
    r = a / b
    return r


primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print(f'{primeiro} + {segundo} = {soma(primeiro, segundo)}')
print(f'{primeiro} - {segundo} = {subtracao(primeiro, segundo)}')
print(f'{primeiro} x {segundo} = {multiplicacao(primeiro,  segundo)}')
print(f'{primeiro} / {segundo} = {divisao(primeiro, segundo):.2f}')


# In[ ]:


#4
def ola(nome):
    print(f'Olá {nome}')


ola(input(f'Digite seu nome: '))


# In[ ]:


#5
from datetime import datetime


def saudacao(nome):
    if datetime.now().hour < 12:
        print(f'Bom dia {nome}')
    elif 12 < datetime.now().hour < 18:
        print(f'Boa tarde {nome}')
    else:
        print(f'Boa noite {nome}')


saudacao(str(input('Digite seu nome: ')))


# In[ ]:


#6
def teste(valor):
    r = bool(valor % 2 == 0)
    return r


print(teste(int(input('Digite um valor: '))))


# In[ ]:


#7
from random import randint


def sorteio():
    lista = list()
    for c in range(0, 10):
        lista.append(randint(0, 100))
    return max(lista)


print(sorteio())


# In[ ]:


#8
from random import randint


def sorteio(valor):
    lista = list()
    for c in range(0, valor):
        lista.append(randint(0, 100))
    return max(lista)


print(sorteio(int(input('Digite um valor: '))))


# In[ ]:


#9


def funcao(lista):
    lista0 = []
    for c in lista:
        lista0.append(c.upper())
    return lista0


print(funcao(str(input('Digite uma frase: ')).split()))


# In[ ]:


#10
from random import randint


def somalista(listaentrada1, listaentrada2):
    listasaida = []
    for k in range(0, 10):
        listasaida.append(listaentrada1[k] + listaentrada2[k])
    return listasaida


#Gerador de lista (linha 13 a linha 17)
lista1 = []
lista2 = []
for c in range(0, 10):
    lista1.append(randint(0, 10))
    lista2.append(randint(0, 10))

print(somalista(lista1, lista2))


# In[ ]:


#11
from random import randint


def multiplicacaolista(listaentrada1, listaentrada2):
    lista3 = []
    for k in range(0, 10):
        lista3.append(listaentrada1[k] * listaentrada2[k])
    return lista3


#Gerador de lista (Linha 13 a linha 17)
lista1 = []
lista2 = []
for c in range(0, 10):
    lista1.append(randint(0, 10))
    lista2.append(randint(0, 10))

print(multiplicacaolista(lista1[:], lista2[:]))


# In[ ]:


#12
from random import randint


def multlista(valor, listaentrada):
    listasaida = []
    for k in listaentrada:
        listasaida.append(k * valor)
    return listasaida


#Gerador de lista (linha 13 a linha 15)
lista = []
for c in range(0, 10):
    lista.append(randint(0, 10))

print(multlista(int(input('Digite um valor: ')), lista[:]))


# In[ ]:


#13
from random import randint


def somalista(listaentrada):
    soma = 0
    for k in listaentrada:
        soma += k
    return soma


#Gerador de lista
lista = []
for c in range(0, 10):
    lista.append(randint(0, 10))

print(somalista(lista))


# In[ ]:


#14
from random import randint


def medialista(listaentrada):
    media = 0
    for k in listaentrada:
        media += k / 2
    return media


#Gerador de lista
lista = []
for c in range(0, 10):
    lista.append(randint(0, 10))

print(medialista(lista))


# In[ ]:


#Desafio 1
def fatorial(n):
    fat = 1
    for k in range(1, n + 1):
        fat *= k
    return fat


print(fatorial(int(input('Digite um valor: '))))


# In[ ]:


#Desafio 2
def validacao(opcao, valor):
    if opcao == 'IDADE':
        if 0 < int(valor) < 150:
            print('Sua Idade é válida')
        else:
            print('Idade inválida')
    elif opcao == 'SALÁRIO' or opcao == 'SALARIO':
        if 0 < float(valor):
            print('Seu Salário é válido')
        else:
            print('Salário inválido')
    elif opcao == 'SEXO':
        if valor[0] in 'MFfmOo':
            print('Seu sexo é válido')
        else:
            print('Sexo inválido')

print('''[IDADE]
[SALÁRIO]
[SEXO]''')
validacao(str(input('Opção: ')).upper().strip(), str(input()))


# In[ ]:


#Desafio 3:
def fibonacci(n):
    n1 = n2 = 1
    n3 = 0
    for c in range(0, n - 2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return n3


print(fibonacci(int(input(f'Digite qual termo deseja: '))))


# In[ ]:


#SUper desafio 1
def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)


print(fat(3))


# In[ ]:


#Super desafio 2
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))


# In[ ]:


#Super Desafio 3
from random import choice


def baralho():
    lista_baralho = []
    for k in range(0, 4):
        lista_baralho.append('Valete')
        lista_baralho.append('Dama')
        lista_baralho.append('Rei')
        lista_baralho.append('Ás')
        for i in range(2, 11):
            lista_baralho.append(i)
    return lista_baralho


def funcao_jogada(dict_, jogador, baralho_, opcao_):
    if opcao_ == 'S':
        valor = choice(baralho_)
        if valor == 'Ás':
            dict_[jogador] += 1
        elif valor == 'Dama' or valor == 'Valete' or valor == 'Dama' or valor == 'Rei':
            dict_[jogador] += 10
        else:
            dict_[jogador] += valor
    else:
        print(f'O jogador {jogador} escolheu não comprar!!')
    return dict_


def funcao_verificar(dict_):
    for key, items in dict_.items():
        if items == 21 or items > 21:
            print(f'{key} --> {items}')
        else:
            print(f'{key} --> {items}')


def funcao_principal():
    # Quantidade e nome dos jogadores
    dict_jogadores = {}
    quant = int(input('Quantos jogadores: '))
    for c in range(0, quant):
        dict_jogadores[f'{str(input("Nome do jogador: ")).upper().strip()}'] = 0
    # Chamar a função para criar o baralho
    baralho_jogo = baralho()
    # Chamar a função da jogada
    cont = cont_empate = 0
    lista_vericacao = []
    jogador_vencedor = ''
    while True:
        while True:
            jogador = str(input('Qual jogador irá jogar: ')).upper().strip()
            if dict_jogadores[jogador] > 21:
                print(f'\033[31mVocê passou de 21, você não pode jogar!!!\033[m')
                break
            elif dict_jogadores[jogador] < 21:
                if cont < quant:
                    opcao_comprar = 'S'
                    funcao_jogada(dict_jogadores, jogador, baralho_jogo, opcao_comprar)
                    print(f'O Jogador {jogador} tem {dict_jogadores[jogador]}')
                    cont += 1
                else:
                    while True:
                        opcao_comprar = str(input('Deseja comprar: '))[0].upper().strip()
                        if opcao_comprar in 'SN':
                            break
                        else:
                            print(f'\033[31mTENTE NOVAMENTE\033[m')
                    funcao_jogada(dict_jogadores, jogador, baralho_jogo, opcao_comprar)
                    print(f'O Jogador {jogador} tem {dict_jogadores[jogador]}')
            print(20 * '--')
            funcao_verificar(dict_jogadores)
            print(20 * '--')
            while True:
                opcao_rodada = str(input(f'Deseja continuar a rodada[SIM ou NÃO]: '))[0].upper().strip()
                print(20 * '--')
                if opcao_rodada in 'SN':
                    break
                else:
                    print(f'\033[31mTENTE NOVAMENTE\033[m')
            if opcao_rodada == 'N':
                break
        for p in dict_jogadores.values():
            lista_vericacao.append(p)
        if max(lista_vericacao) > 21:
            lista_vericacao.remove(max(lista_vericacao))
        elif max(lista_vericacao) < 21 or max(lista_vericacao) == 21:
            valor_vencendor = max(lista_vericacao)
            for w in lista_vericacao:
                if w == valor_vencendor:
                    cont_empate += 1
            if cont_empate == 1:
                for key, items in dict_jogadores.items():
                    if items == valor_vencendor:
                        jogador_vencedor = key
                print(f'O jogador vencedor foi {jogador_vencedor}')
                break
            elif cont > 1:
                print(f'O jogo deu empate')
                break
        break

print(20 * '--')
print(f'{"BlackJack":^40}')
print(20 * '--')
funcao_principal()


# In[ ]:


#Super desafio 4
def cadastro_cliente(clientes_):
    lista_cliente = [str(input('Nome: '))]
    while True:
        cpf = str(input('CPF: '))
        if len(cpf) == 11 and cpf.isalnum():
            break
        else:
            print(f'\033[31mTENTE NOVAMENTE\033[m')
    lista_cliente.append(cpf)
    lista_cliente.append(str(input('E-mail: ')))
    clientes_.append(lista_cliente[:])
    lista_cliente.clear()
    print(clientes_)
    return clientes_


def funcao_vereficar(lista, cpf_):
    for c in range(0, len(lista)):
        if lista[c][1] == cpf_:
            print(lista[c])
            break
        elif:
            print(f'\033[31mNÃO ENCONTRADO\033[m')



print(20 * '--')
print(f'{"Sistema":^40}')
print(20 * '--')
print('''[0] --> Parar
[1] --> Cadastro de Cliente
[2] --> Verificar Cliente''')
lista_geral = []
while True:
    while True:
        opcao = str(input('Digite sua opcao: ')).strip()
        if opcao in '012':
            break
        else:
            print(f'\033[31mTENTE NOVAMENTE\033[m')
    if opcao == '0':
        break
    elif opcao == '1':
        cadastro_cliente(lista_geral)
    elif opcao == '2':
        while True:
            cpf_cliente = str(input('CPF: '))
            if len(cpf_cliente) == 11 and cpf_cliente.isalnum():
                break
            else:
                print(f'\033[31mTENTE NOVAMENTE\033[m')
        funcao_vereficar(lista_geral, cpf_cliente)


# In[ ]:




