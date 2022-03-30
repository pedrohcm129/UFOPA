#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
palavra = str(input('Digite uma palavra: '))
for letra in palavra:
    print(letra)


# In[ ]:


#2
palavra = str(input('Digite uma palavra: '))
novapalavra = ''
for letra in palavra:
    novapalavra += letra
print(novapalavra)


# In[ ]:


#3
palavra = str(input('Digite uma palavra: '))
novapalavra = ''
for letra in range(0, len(palavra)):
    if letra % 2 == 0:
        novapalavra += palavra[letra].upper()
    else:
        novapalavra += palavra[letra].lower()
print(novapalavra)


# In[ ]:


#4
palavra = str(input('Digite uma palavra: '))
novapalavra = ''
for letra in palavra:
    novapalavra += letra + ' '
print(novapalavra.strip())


# In[ ]:


#5
palavra = str(input('Digite uma palavra: '))
novapalavra = ''
for c in palavra:
    if c == 'a':
        c = '4'
    elif c == 'e':
        c = '3'
    elif c == 'l':
        c = '1'
    elif c == 't':
        c = '7'
    novapalavra += c
print(novapalavra)


# In[ ]:


#6
palavra = str(input('Digite uma palavra: '))
print(palavra[::-1])


# In[ ]:


#7
palavra = str(input('Digite uma palavra: '))
if palavra == palavra[::-1]:
    print(f'Sua palavra {palavra} é um palíndromo')
else:
    print(f'A palavra {palavra}/{palavra[::-1]} não é um palíndromo')    


# In[ ]:


#8
texto = str(input('Digite um texto: '))
palavra = str(input('Digite aqui a palavra que você quer que seja encontrada: '))
print(palavra in texto)


# In[ ]:


#9
palavra = str(input('Digite uma palavra/frase: '))
palavraletra = ''
palavranumero = ''
for letra in palavra:
    if letra in 'abcdefghijklmnopqrstuvxzABCDEFGHIJKLMNOPQRSTUVXZ':
        palavraletra += letra
    if letra in '1234567890':
        palavranumero += letra
print(f'{palavra}, {palavraletra}, {palavranumero}')


# In[4]:


#Desafio
palavra = str(input('Digite uma palavra: '))
letra = str(input('Digite uma letra: '))
cont = u = p = 0
for c in range(0, len(palavra)):
    if palavra[c] == letra:
        print(f'Posição {c + 1}')
        if cont == 0:
            u = c
            p = c
        else:
            if c < p:
                p = c
            if c > u:
                u = c
        cont += 1
print(f'A quantidade de vezes que a letra {letra} apareceu foi {cont}')
print(f'A distância entra as duas é de {u - p} caracteres')


# In[4]:


#superdesafio
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
criptografia = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'p', 'q', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
novapalavra = ''
palavra = str(input('Digite uma palavra para ser criptografada: ')).lower()
for letra in palavra:
    if letra in letras:
        novapalavra += criptografia[letras.index(letra)]
print(f'A palavra {palavra} criptografada é {novapalavra}')

