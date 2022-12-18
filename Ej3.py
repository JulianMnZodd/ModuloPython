print('Ingrese su peso: ')
peso=float(input())
print('Ingrese su altura en metros: ')
altura=float(input())

indice=peso/pow(altura,2)

print('Tu índice de masa corporal es: '+str(round(indice,2)))