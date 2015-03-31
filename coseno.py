import sys
from sets import Set
from numpy import dot
from numpy.linalg import norm


#def remuevoDuplicados(lista):
#	""" remuevo duplicados de la lista """
#	return Set((item for item in lista))


def coseno(vector1, vector2):
	""" relacion de documentos con el concepto comparando vectores con regla del coseno :
		coseno  = ( V1 * V2 ) / ||V1|| x ||V2|| """
	return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))

