print('Matrícula: 2021004856')
print('Base: 11')
print('-' * 21)
valor = int(input('Digite um valor: '))
print('-' * 21)
base = 11
valor_convertido = ''
while True:
    resto = valor % base
    if resto == 10:
        valor_convertido += str('A')
    else:
        valor_convertido += str(resto)
    if valor // base == 0:
        break
    valor //= base
print(f'Resultado = {valor_convertido[::-1]}')
print('-' * 21)