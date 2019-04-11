file = open('pruebas.txt','r')

texto = file.read()

k = 0
j = 0
borrar2 = 0
for i in range(0,len(texto)-1):
	if(texto[i] == '<'):
		borrar = i
	if(texto[j] == '>'):
		borrar2 = j

	texto = texto[:borrar-1] + texto[borrar2:]

print(texto)		