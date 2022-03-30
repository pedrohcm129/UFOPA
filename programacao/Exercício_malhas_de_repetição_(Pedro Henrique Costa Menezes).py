#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
num = int(input('Digite um número: '))
cont = 0
while cont != num:
    cont += 1
    print(cont)


# In[ ]:


#2
num = int(input('Digite um número: '))
cont = num
fat = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat = fat * cont
    cont -= 1
print(fat)


# In[ ]:


#3
num = int(input('Digite um número: '))
cont = 0
soma = 0
while cont != num:
    cont += 1
    soma += cont
print(soma)


# In[ ]:


#4
cont = 0
resultado = 1
while cont != 10:
    cont += 1
    resultado = cont * 9
    print(f'9 x {cont} = {resultado}')


# In[ ]:


# 5
soma = 0
while True:
    num = int(input("Digite um valor [0 para parar]: "))
    soma += num
    if num == 0:
        break
print(f'A soma dos números é {soma}')


# In[ ]:


#6
from random import randint
maquina = randint(1, 10)
num = -1
while num != maquina:
    num = int(input('Digite um número: '))
    if num != maquina:
        print('\033[31mERRO!!!\033[m')
print(f'Você acertou o número da máquina era {maquina}')


# In[ ]:


#7
idade = salario = cont = 0
sexo = ''
while True:
    while True:
        idade = int(input('Digite o valor da sua idade: '))
        if 0 < idade < 150:
            print(f'Sua idade é {idade}')
            break
        print('\033[31mERRO!!!!!!\033[m\nTente novamente')
    while True:
        salario = float(input('Digite o valor do seu salário: '))
        if salario > 0:
            print(f'Seu salário é {salario}')
            break
        print('\033[31mERRO!!!!!!\033[m\nTente novamente')
    while True:
        sexo = str(input('Digite seu sexo [M/F/OUTRO]: ')).upper().strip()
        if sexo in 'MFOUTRO':
            print(f'Seu sexo é {sexo}')
            break
        print('\033[31mERRO!!!!!!\033[m\nTente novamente')
    break


# In[ ]:


#Desafio 1
soma = 0
cont = -1
numerador = 1
while cont != 1000:
    cont += 1
    numerador /= 2
    soma += numerador
print(f'Sua soma é {soma}')


# In[ ]:


#Super Desafio!
cont = 1000
soma = num = 0
fat = numerador = 1.0
while cont != 0:
    num = cont
    while num != 0:
        fat *= num
        num -= 1
    numerador = 1 / fat
    soma += numerador
    cont -= 1
print(soma)
#Não tenho certeza se está certo...

