class Alumno:
    nombre=''
    nota=0
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def evaluar(self):
        if(self.nota>=6):
            print('Aprobó')
        else:
            print('Desaprobó')
    
    def imprimirDatos(self):
        print('El nombre del alumno es:',self.nombre+ ' y su nota es:',self.nota)
        self.evaluar()
        
alumno1 = Alumno('Pedrito',10)

alumno1.imprimirDatos()