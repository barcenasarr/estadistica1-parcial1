#import matplotlib.pyplot as plt
import numpy
from collections import Counter

def obtener_datos():
	archivo = open("datos.txt","r")
	archivo.seek(0)
	datos1 = archivo.read().split()
	archivo.close()

	i = 1
	j = 0
	k = 0
	global datos2
	global N
	datos2 = []
	N = len(datos1)/2
	print "Materias (N): ", N
	while k < N:
		datos2.append([int(datos1[i]), datos1[j]])
		i += 2
		j += 2
		k += 1
	datos2.sort(key = lambda x: (x[0], x[1]))
	print "\n"
	for elem in datos2:
		print elem

def obtener_Xi():
	k = 0
	global Xi
	Xi = []
	while k < N:
		Xi.append(datos2[k][0])
		k += 1
	"""for elem in Xi:
		print elem"""

def obtener_ni():
	global ni
	ni = [[x,Xi.count(x)] for x in set(Xi)]
	ni.sort(key = lambda x: x[0])
	"""for elem in ni:
		print elem"""

def organizar_Xi():
	global Xi2
	Xi2 = []
	k = 0
	while k < len(ni):
		Xi2.append(ni[k][0])
		k += 1
	"""for elem in Xi2:
		print elem"""

def obtener_fi():
	k = 0
	global fi
	fi = []
	while k < len(ni):
		aux = float(ni[k][1]) / N
		fi.append(aux)
		k += 1

def obtener_Ni():
	k = 0
	aux = 0
	global Ni
	Ni = []
	while k < len(ni):
		aux += ni[k][1]
		Ni.append(aux)
		k += 1

def obtener_Fi():
	k = 0
	aux = 0
	global Fi
	Fi = []
	while k < len(Ni):
		aux = float(Ni[k]) / N
		Fi.append(aux)
		k += 1

def imprimir_tabla():
	k = 0
	global tabla
	tabla = []
	while k < len(ni):
		tabla.append([Xi2[k], ni[k][1], fi[k], Ni[k], Fi[k]])
		k += 1
	print "\nXi\t ni\t fi\t Ni\t Fi"
	for elem in tabla:	
		print "%d\t %d\t %.2f\t %d\t %.2f" % (elem[0], elem[1], elem[2], elem[3], elem[4])

def media():
	k = 0
	global media
	global suma
	suma = 0
	while k < len(ni):
		aux = ni[k][0] * ni[k][1]
		suma += aux
		k += 1
	media = float(suma) / N
	print "\nMedia: ", media

def mediana(lst):
	print "Mediana: ", numpy.median(numpy.array(lst))

def moda(a):
	b = Counter(a)
	print "Moda: ", b.most_common(1)[0][0]

"""def graficas():
	x = [1,2,3]
	y = [[1,2,3],[4,5,6],[7,8,9]]
	plt.xlabel("X-axis")
	plt.ylabel("Y-axis")
	plt.title("A test graph")
	for i in range(len(y)):
		plt.plot(Xi2,[pt[i] for pt in y],label = 'id %s'%i)
	plt.legend()
	plt.show()"""

obtener_datos()
obtener_Xi()
obtener_ni()
organizar_Xi()
obtener_fi()
obtener_Ni()
obtener_Fi()
imprimir_tabla()
media()
mediana(Xi2)
moda(Xi)
#graficas()
