print('Ingrese su peso: ')
peso=float(input())
print('Ingrese su altura en metros: ')
altura=float(input())

indice=peso/pow(altura,2)

print(f'Tu índice de masa corporal es: {round(indice,2)}')