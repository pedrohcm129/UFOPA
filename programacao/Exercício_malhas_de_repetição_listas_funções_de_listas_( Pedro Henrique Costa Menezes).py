#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
lista = [1, 5, 123.2434, 'Pedro']
for c in lista:
    print(c)


# In[ ]:


#2
lista = [1, 56, 34, 2, 3]
cont = 0
while len(lista) != cont:
    print(lista[cont])
    cont += 1


# In[ ]:


#3
lista = []
cont = 0
num = int(input('Digite um valor: '))
while num != cont:
    lista.append(cont)
    cont += 1
print(lista)


# In[ ]:


#4
lista = [1, 34, 56, 23, 54, 5412, 323, 42234, 456, 4, 5]
cont = 0
cont1 = 0
while cont != len(lista):
    if lista[cont] % 2 == 0:
        cont1 += 1
    cont += 1
print(f'A quantidade de números pares na lista {lista} é {cont1}')


# In[ ]:


#5
lista = [1, 34, 56, 23, 54, 5412, 323, 42234, 456, 4, 5]
cont = 0
maior = 0
while cont != len(lista):
    n = lista[cont]
    if (cont == 0) or (maior < n):
        maior = n
    cont += 1
print(maior)


# In[ ]:


#6
lista = [1, 34, 56, 23, 54, 5412, 323, 42234, 456, 4, 5]
for c in range(0, 3):
    print(max(lista))
    lista.remove(max(lista


# In[ ]:


#7
lista1 = [1, 34, 56, 23, 54, 5412, 323, 42234, 456, 4, 5]
lista2 = [293, 567, 99, 283, 45994, 996, 494, 988, 394, 2930, 688]
lista3 = []
valor = 0
'''cont = 0
while cont != 11:
    valor = lista1[cont] + lista2[cont]
    lista3.append(valor)
    cont += 1
print(lista3)'''
for c in range(0, len(lista1)):
    valor = lista1[c] + lista2[c]
    lista3.append(valor)
print(lista3)


# In[ ]:


#8
lista2 = [293, 567, 99, 283, 45994, 996, 494, 988, 394, 2930, 688]
lista1 = [1, 34, 56, 23, 54, 5412, 323, 42234, 456, 4, 5]
soma = 0
for c in range(0, len(lista1)):
    ps = lista2[c] * lista1[c]
    soma += ps
print(f'O produto escalar é {soma}')


# In[ ]:


#9
lista = []
for c in range(0, 6):
    num = input(f'Digite o valor {c} para ser adicionado a lista: ')
    lista.append(num)
print(lista)


# In[ ]:


#10
lista = []
for c in range(0, 6):
    num = input(f'Digite o valor {c} para ser adicionado a lista: ')
    lista.append(float(num))
print(lista)


# In[ ]:


#11
media = 0
lista = []
for c in range(0, 4):
    nota = float(input(f'Digite a nota {c + 1}: '))
    lista.append(nota)
    media += nota / 4
print(f'Sua média foi {media} e as suas notas foram {lista}')


# In[ ]:


#12
from random import randint
cont = 0
lista = []
while cont != 10:
    cont += 1
    lista.append((randint(0, 100)))
print(lista)
print(lista[0:4:1])
print(lista[len(lista) - 5:len(lista):1])
print(lista[3:len(lista):2])
print(lista.reverse())
print(lista[5:0:1].reverse())
print(lista[len(lista) - 5:len(lista):1].reverse())
#Não consegui utilizar o comando 'reverse()'


# In[ ]:


#13
from random import randint
cont = 0
cont50 = 0
while cont != 10:
    cont += 1
    n = randint(0, 100)
    print(n)
    if n > 50:
        cont50 += 1
print(cont50)


# In[ ]:


#14
from random import randint
maior = menor = soma = cont = 0
for c in range(0, 10):
    num = randint(0, 100)
    print(num)
    soma += num
    if menor == 0:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = soma / 10
print(f'O maior número foi {maior}, já o menor foi {menor}, a soma foi {soma} e a média foi {media}.')


# In[ ]:


#Desafio 1
nome = str(input('Nome do aluno: '))
idade = int(input('Idade: '))
quant = int(input('Quantidade de provas: '))
lista = []
lista1 =[]
media = 0
for c in range(0, quant):
    nota = float(input(f'Nota {c + 1}: '))
    lista.append(nota)
    media += nota / quant
lista1.append(nome)
lista1.append(idade)
lista1.append(lista)
lista1.append(media)
lista1.append(media > 5)
print(lista1)


# In[ ]:


#Desafio 2
nome = str(input('Nome do aluno: '))
idade = int(input('Idade: '))
quant = int(input('Quantidade de provas: '))
lista = []
lista1 = []
media = 0
for c in range(0, quant):
    nota = float(input(f'Nota {c + 1}: '))
    lista.append(nota)
    media += nota / quant
lista1.append(nome)
lista1.append(idade)
lista.remove(max(lista))
lista.remove(min(lista))
lista1.append(lista)
lista1.append(media)
lista1.append(media > 5)
print(lista1)


# In[ ]:


#Desafio 3
while True:
    cpf = str(input('Digite seu CPF [APENAS NÚMEROS]: '))
    if len(cpf) == 11:
        break
cont = x = s = q = 0
for c in range(10, 1, -1):
    n = int(cpf[cont]) * c
    cont += 1
    x += n
if (x * 10) % 11 == int(cpf[9]):
    for t in range(11, 1, -1):
        r = int(cpf[q]) * t
        q += 1
        s += r
    if (s * 10) % 11 == int(cpf[10]):
        print(f'Seu CPF {cpf} é válido')
    else:
        print(f'Seu CPF {cpf} não é válido')

