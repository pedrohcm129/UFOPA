print(30 * '-')
print('Triângulo')
print(30 * '-')

lado_um = float(input('1° Lado: '))
lado_dois = float(input('2° Lado: '))
lado_tres = float(input('3° Lado: '))
semiperimetro = (lado_dois + lado_tres + lado_um) / 2
areaX = (semiperimetro * (semiperimetro - lado_um) * (semiperimetro -  lado_dois) * (semiperimetro - lado_tres)) ** (1 / 2)
print(f'Área x: {areaX:.4f}')

print(30 * '-')

lado_um = float(input('1° Lado: '))
lado_dois = float(input('2° Lado: '))
lado_tres = float(input('3° Lado: '))
semiperimetro = (lado_dois + lado_tres + lado_um) / 2
areaY = (semiperimetro * (semiperimetro - lado_um) * (semiperimetro -  lado_dois) * (semiperimetro - lado_tres)) ** (1 / 2)
print(f'Área Y: {areaY:.4f}')

print(30 * '-')

if areaX == areaY:
    print('Os triângulos são iguais.')
elif areaX > areaY:
    print('X > Y')
else:
    print('Y > X')
print(30 * '-')