import time
hrlocal=time.localtime()

def irAcasa():
    print('la hora actual es:', time.strftime('%H:%M',time.localtime()))
    if(hrlocal.tm_hour>19):
        print('Puede ir a casa')
    else:
        h= 18-hrlocal.tm_hour
        m=60-hrlocal.tm_min
        tiempo=f'{h}hs y {m} minutos'
        print(f'le quedan {tiempo} de trabajo')
        
irAcasa()

        

