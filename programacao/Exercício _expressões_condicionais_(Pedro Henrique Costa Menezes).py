#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
idade = int(input('Digite aqui a sua idade: '))
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')


# In[ ]:


#2
numero = float(input('Digite um número: '))
if numero > 0.0:
    print('Seu número é positivo')
elif numero == 0.0:
    print('Seu número é {0:.0f} e é neutro'.format(numero))
else:
    print('O seu número é negativo')


# In[ ]:


#3
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
if num1 > num2:
    print('O maior número é {0}\nO menor número é {1}'.format(num1, num2))
elif num2 > num1:
    print('O maior número é {0}\nO menor número é {1}'.format(num2, num1))
else:
    print('Seus números são iguais')


# In[ ]:


#4
idade = int(input('Digite aqui o valor da sua idade, entre 0 e 150 anos: '))
if 0 < idade < 150:
    print('Sua idade é {0} anos'.format(idade))
else:
    print('ERRO')
salario = float(input('Digite aqui o valor do seu salário: '))
if salario > 0: 
    print('Seu salário é {0}'.format(salario))
else:
    print('ERRO')
print('''M: Para masculino
F: Para feminino
Outro: Para outro tipo de sexo''')    
sexo = str(input('Digite aqui seu sexo:')).strip()
sexo = sexo.upper()
if sexo == 'F':
    print('Você é mulher')
elif sexo == 'M':
    print('Você é um homem')
elif sexo == 'OUTRO':
    print('Você não se indentifica com nenhum dos gêneros')
else:
    print('ERRO')


# In[ ]:


#5 
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('Sua média é {}'.format(media))
if media >= 6.0:
    print('Você passou!!!\nParabêns')
else:
    print('Você não passou!!!\nEstude mais')


# In[ ]:


#6
print('''(Enem) O despejo de dejetos de esgotos domésticos e industriais vem causando sérios problemas aos rios brasileiros. Esses poluentes são ricos em substâncias que contribuem para a eutrofização de ecossistemas, que é um enriquecimento da água por nutrientes, o que provoca um grande crescimento bacteriano e, por fim, pode promover escassez de oxigênio.

Uma maneira de evitar a diminuição da concentração de oxigênio no ambiente é:

a) Aquecer as águas dos rios para aumentar a velocidade de decomposição dos dejetos.

b) Retirar do esgoto os materiais ricos em nutrientes para diminuir a sua concentração nos rios.

c) Adicionar bactérias anaeróbicas às águas dos rios para que elas sobrevivam mesmo sem oxigênio.

d) Substituir produtos não degradáveis por biodegradáveis para que as bactérias possam utilizar os nutrientes.

e) Aumentar a solubilidade dos dejetos no esgoto para que os nutrientes fiquem mais acessíveis às bactérias.''')
opcao = str(input('Digite aqui sua alternativa: ')).strip().upper()
if opcao == 'A' or opcao == 'C' or opcao == 'D':
    print('A opção {0}, está errada!!'.format(opcao))
elif opcao == 'B': 
    print('A opcão {0}, está certa'.format(opcao))
else:
    print('Você não escolheu nenhuma das alternativas')


# In[ ]:


#7
print('QUESTIONÁRIO DA POLÍCIA')
print('Apenas respostas de sim ou não')
p1 = str(input('Mora perto da vítima? ')).strip().upper()
p2 = str(input('Já trabalhou com a vítima? ')).strip().upper()
p3 = str(input('Telefonou para a vítima? ')).strip().upper()
p4 = str(input('Esteve no local do crime? ')).strip().upper()
p5 = str(input('Devia para a vítima? ')).strip().upper()
if p1 == 'SIM':
    p1 = 1
elif p1 == 'NÃO' or 'NAO':
    p1 = 0
if p2 == 'SIM':
    p2 = 1
elif p2 == 'NÃO' or 'NAO':
    p2 = 0
if p3 == 'SIM':
    p3 = 1
elif p3 == 'NÃO' or 'NAO':
    p3 = 0
if p4 == 'SIM':
    p4 = 1
elif p4 == 'NÃO' or 'NAO':
    p4 = 0
if p5 == 'SIM':
    p5 = 1
elif p5 == 'NÃO' or 'NAO':
    p5 = 0
soma = (p1 + p2 + p3 + p4 + p5)
if soma == 5:
    print('Você é o assassino')
elif soma == 3 or soma == 4:
    print('Você é cumplície')
elif soma == 2:
    print('Você é suspeito')
elif soma == 0 or soma == 1:
    print('Você esta liberado')


# In[ ]:


#8
preco = float(input('Digite aqui o valor antigo: '))
if preco <= 50:
    preco = preco * 1.05
elif 50 < preco < 100:
    preco = preco * 1.10
elif 100 <= preco <= 150:
    preco = preco * 1.13
elif preco > 150:
    preco = preco * 1.15
print('O novo preço é {0:.2f}'.format(preco))
if preco <= 80:
    print('Barato')
elif 80 < preco <= 115:
    print('Razoável')
elif 115 < preco <= 150:
    print('Normal')
elif 150 < preco <= 170:
    print('Caro')
elif preco > 170:
    print('Muito caro')


# In[ ]:


#Desafio 1
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 > n2 > n3 or n1 > n3 > n2:
    print('O maior valor é {}'.format(n1))
elif n2 > n1 > n3 or n2 > n3 > n1:
    print('O maior valor é {}'.format(n2))
elif n3 > n1 > n2 or n3 > n2 > n1:
    print('O maior valor é {}'.format(n3))


# In[ ]:


#Desafio 2
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
n4 = float(input('Quarto número: '))
if n1 > n2 > n3 > n4 or n1 > n2 > n4 > n3 or n1 > n3 > n2 > n4 or n1 > n3 > n4 > n2 or n1 > n4 > n2 > n3 or n1 > n4 > n3 > n2:
    print('O maior valor é {}'.format(n1))
elif n2 > n1 > n3 > n4 or n2 > n1 > n3 > n4 or n2 > n3 > n1 > n4 or n2 > n3 > n4 > n1 or n2 > n4 > n1 > n3 or n2 > n4 > n3 > n1:
    print('O maior valor é {}'.format(n2))
elif n3 > n1 > n2 > n4 or n3 > n1 > n2 > n4 or n3 > n2 > n1 > n4 or n3 > n2 > n4 > n1 or n3 > n4 > n1 > n2 or n3 > n4 > n2 > n1:
    print('O maior valor é {}'.format(n3))
else:
    print('O maior valor é {}'.format(n4))


# In[ ]:


#Desafio 3
print('\033[0;31mQUESTIONÁRIO PARA DIAGNÓSTICO\033[m')
print('RESPOSTAS DE SIM OU NÃO')
p1 = str(input('Sente dor no corpo? ')).strip().upper()
p2 = str(input('Você tem febre? ')).strip().upper()
p3 = str(input('Você tem tose? ')).strip().upper()
p4 = str(input('Esta com congestão nasal? ')).strip().upper()
p5 = str(input('Tem manchas no corpo? ')).strip().upper()
#Denge
if (p1 == 'SIM') and (p2 == 'SIM') and (p3 == 'NÃO' or p3 == 'NAO') and (p4 == 'NÃO' or p4 == 'NAO') and (p5 == 'SIM'):
    print('Você está com denge')
#Gripe
elif ((p1 == 'SIM') and (p2 == 'SIM') and (p3 == 'SIM') and (p4 == 'SIM') and (p5 == 'NÃO' or p5 == 'NAO')) or ((p1 == 'NÃO' or p1 == 'NAO') and (p2 == 'SIM') and (p3 == 'SIM') and (p4 == 'SIM') and (p5 == 'NÃO' or p5 == 'NAO')):
    print('Você está com gripe')
else:
    print('Você está não está doente')


# In[ ]:




