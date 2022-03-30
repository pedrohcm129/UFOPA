primeiro_numero = int(input('Digite o 1° valor: '))
segundo_numero = int(input('Digite o 2° valor: '))
if not (primeiro_numero % segundo_numero) and (segundo_numero // primeiro_numero) and (primeiro_numero // segundo_numero):
    print(f'{primeiro_numero} = {segundo_numero}')
elif primeiro_numero // segundo_numero :
    print(f'{primeiro_numero} > {segundo_numero}')
elif segundo_numero // primeiro_numero:
    print(f'{primeiro_numero} < {segundo_numero}')