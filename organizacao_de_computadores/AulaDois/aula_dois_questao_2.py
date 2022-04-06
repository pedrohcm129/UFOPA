lista = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9,]
soma = 0
lista_copia = lista.copy()
for indice in range(0, 10):
    lista[indice] = lista_copia[9 - indice]
    if indice % 2 == 0 and indice != 0:
        soma += lista[indice]
    else:
        continue
del lista_copia
print(lista)
print(f'A soma dos valores de indice par: {soma}')