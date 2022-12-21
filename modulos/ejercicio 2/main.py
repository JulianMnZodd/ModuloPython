"""suponiendo que trabajo 7 horas desde las 0 a las 7"""
import time
hrlocal=time.localtime()

def irAcasa():
    print('la hora actual es:', time.strftime('%H:%M:%S',time.localtime()))
    if(hrlocal.tm_hour>7):
        print('Puede ir a casa')
    else:
        tiempo= 7-hrlocal.tm_hour
        print('le quedan',str(tiempo)+'hr de trabajo')
        
irAcasa()

        

