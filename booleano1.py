import collections
from hash import eagles
from coseno import coseno
import math
from numpy.linalg import norm


#Logica para abrir archivo
ar1=open('respuesta_tres_detenidos_por_caso_Heaven.txt', 'r')#.read().split()

ar2=open('respuesta_muere_Johnny_Laboriel.txt', 'r')#.read().split()

arc=open('respuesta_Muere_Johnny_Laboriel.txt', 'r')#.read().split()

#Las palabras separadas por comas se asignan a una lista
ResultadoDoc1 = [line.split() for line in ar1.readlines()]
ResultadoDoc2 = [line.split() for line in ar2.readlines()]
ResultadoConsulta = [line.split() for line in arc.readlines()]

#Remueve caracteres indeseables de cada lista generada con las palabras de documentos
# como '"','"','Fe','1'.
signosIndeseables = ['"','"','Fe','1','Fz','Fit','*','+','-','/']
RD1 = [x for x in ResultadoDoc1 if x != signosIndeseables]
rd1 = [x for x in RD1 if x ]

RD2 = [x for x in ResultadoDoc2 if x != signosIndeseables]
rd2 = [x for x in RD2 if x ]

RDC = [x for x in ResultadoConsulta if x != signosIndeseables]
rd3 = [x for x in RDC if x ]

##print 'Contenido de documento rd1'
##print(rd1)
##print 'Contenido de documento rd2'
##print(rd2)
##print 'Contenido de documento consulta'
##print(rd3)


#Convierto a dictionario
eagles_dict = dict(eagles)


################################
#Funcion que compara las etiquetas de cada palabra y también compara si la palabra
#aparece más de una vez compara nuevamente su etiqueta para validar su diferencia
#semántica.

#Acepta como argumento las listas de palabras y etiquetas
#Regresa una lista de listas con las palabras aceptadas por la condición,
#su etiqueta y el número de palabras
def compara(lista):
    listaPalabras=[]
    res = []
    result = []
    for item in lista:
        if item[2] in eagles_dict.keys():
            listaPalabras.append(item[1])
    return listaPalabras

#remueve duplicados
lista1 = list(set(compara(rd1)))
lista2 = list(set(compara(rd2)))
lista3 = list(set(compara(rd3)))



def vector1(l1, l2, l3):
    listaTotal = l1 + l2 + l3
    di = {}
    ks = [x for x in range(1, len(listaTotal))]
    d1 = dict(zip(ks, listaTotal))
    for value in d1.values:
        if value in l1:
            li.append(1)
        else:
            li.append(0)
    return li

print(vector1(lista1, lista2, lista3))


