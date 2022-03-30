#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
print('Olá Mundo')


# In[2]:


#2
numero = input('Digite um número: ')
print(numero)


# In[6]:


#3
from math import trunc
numero = input('Digite um número: ')
print(float(numero))
print(trunc(float(numero)))
# Não consegui transformar str em um int, portanto,  o comando "trunc",foi utilizado para tranformar um possível número real em inteiro.


# In[9]:


#4
n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
soma = (n1 + n2)
print('Sua soma é: {}'.format(soma))


# In[10]:


#5
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 +  nota4)/4
print('O valor da média das quatro notas é: {:.2f}'.format(media))


# In[13]:


#6
from math import pi
raio = float(input('Digite o valor do raio a circunferência: '))
area = (raio**2)*pi
print('O valor da área da circunferência de raio {0}, é {1:.2f}'.format(raio, area))


# In[16]:


#7
ganhohora = float(input('Quanto é ganho por hora de trabalho?? '))
hora = float(input('Quantas hora é trabalhada?? '))
print('O valor ganhado é: R${:.1f}'.format(hora*ganhohora))


# In[18]:


#8
tempf = float(input('Digite aqui a temperatura em fanhrenheit: '))
tempc = (tempf-32)*5/9
print('A temperatura em graus celsius é de: {:.2f}'.format(tempc))


# In[19]:


#9
dia = int(input('Digite o dia do seu aniversário: '))
mes = int(input('Digite o mês do seu aniversário: '))
ano = int(input('Digite o seu ano de nascimento: '))
print('A data do seu nascimento foi: {0}/{1}/{2}'.format(dia, mes, ano))


# In[5]:


#10
int1 = int(input('Primeiro número inteiro: '))
int2 = int(input('Segundo número inteiro: '))
real = float(input('Digite um número real: '))
n1 = (int1 * int2)
n2 = (int2*3) + real
n3 = (float1**3)
print('O produto do dobro do primeiro com metade do segundo: {0}\nA soma do triplo do primeiro com o terceiro: {1}\nO terceiro elevado ao cubo: {2}'.format(n1, n2, n3))


# # 

# In[8]:


#11
massa = float(input("Digite aqui o valor da sua massa: "))
altura = float(input('Digite o valor da sua altura: '))
imc = massa/(altura**2)
print('Seu IMC vale: {0:.1f}'.format(imc))


# In[12]:


#12
valor = float(input('Digite o valor a ser aumentado: '))
aumentado = valor*1.15
print('O novo valor é {0:.1f}'.format(aumentado))


# In[13]:


#13
valor = float(input('Digite o valor a ser aumentado: '))
diminuido = valor * 0.85
print('O novo valor é {0:.1f}'.format(diminuido))


# In[15]:


#Desafio 1
velocidade = float(input('Digite a velocidade em m/s(metros por segundo): '))
inicioposicao = float(input('Digite a posição inicial em m(metros): '))
instante = float(input('Digite o instante de tempo em s(segundo): '))
final = inicioposicao+velocidade*instante+(-5*(instante**2))
print('A posição final é {:.2f}'.format(final))


# In[16]:


#Desafio 2
from datetime import datetime
print(datetime.now())

