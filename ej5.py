def esBisiesto(anio):
    if(anio %4 ==0 and anio %100 !=0):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} no es bisiesto')
        
anio = int(input('Ingrese un año: '))
esBisiesto(anio)