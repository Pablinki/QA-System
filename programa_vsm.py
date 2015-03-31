from numpy import dot
from numpy.linalg import norm
import math
# -*- coding: utf-8 -*-

#Logica para abrir archivo
ar=open('prueba_docs.txt', 'r').read().split()

#Logica para cambiar a mayusculas
ar_min= [x.lower() for x in ar]

#comparar listas
#def 
#for el in range(0,len(ar_min)):
#   if el in ar

doc1 ="Mañana será un día estupendo, me voy de pesca"
doc2 ="Me gusta mas la noche que el día"
doc3 ="Paco será alguien el día de mañana"
consulta= "Me gusta alguien"

terminos = ["Mañana","será","un","día","estupendo","me","voy","de","pesca","gusta","mas","la","noche","alguien"]

doct1=[1,1,1,1,1,1,1,1,1,0,0,0,0,0]
doct2=[0,0,0,1,0,1,0,0,0,1,1,1,0,0]
doct3=[1,1,0,1,0,0,0,0,0,0,0,1,1,1]
consulta_t=[0,0,0,0,0,1,0,0,0,1,0,0,0,1]

#Normalizacion
def cuadrado(n):
    return n ** 2

def sumarLista(lista):
    sum=0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum



# calculo coseno

def coseno(vector1, vector2):
    """coseno  = ( V1 * V2 ) / ||V1|| x ||V2|| """
    #return float(dot(vector1,vector2) / (math.sqrt(sumarLista(map(cuadrado,vector1))) * math.sqrt(sumarLista(map(cuadrado,vector2))))
    return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))



r1 = coseno(consulta_t,doct1)
r2 = coseno(consulta_t,doct2)
r3 = coseno(consulta_t,doct3)

print(r1)
print(r2)
print(r3)
                     






