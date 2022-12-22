import pprint
#fichero = open('fichero.txt','x')
f=open('fichero.txt','w')
f.write('Hola desde python!\n')
f.close()

f= open('fichero.txt','r+')
f.readline()
f.write('Hola de nuevo!\n')

f.seek(0)

pprint.pprint(f.read())
f.close()
