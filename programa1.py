import collections
from hash import eagles
from coseno import coseno
import math
from numpy.linalg import norm
#from tf_idf import programa2

#Logica para abrir archivo
ar1=open('res_alain_delon.txt', 'r')#.read().split()
ar2=open('res_alerta_mex.txt', 'r')#.read().split()
ar3=open('res_cae_de_bici.txt', 'r')#.read().split()
ar4=open('res_chapo_rico.txt', 'r')#.read().split()
ar5=open('res_cineasta.txt', 'r')#.read().split()
ar6=open('res_cnte.txt', 'r')#.read().split()
ar7=open('res_mov_autodef.txt', 'r')#.read().split()
ar8=open('res_desaloja_zoc.txt', 'r')#.read().split()
ar9=open('res_detiene_poli.txt', 'r')#.read().split()
ar10=open('res_esp_recomineda.txt', 'r')#.read().split()
ar11=open('res_homb_muerto.txt', 'r')#.read().split()
ar12=open('res_ing_mex.txt', 'r')#.read().split()
ar13=open('res_alain_delon.txt', 'r')#.read().split()
ar14=open('res_alerta_mex.txt', 'r')#.read().split()
ar15=open('res_cae_de_bici.txt', 'r')#.read().split()
ar16=open('res_chapo_rico.txt', 'r')#.read().split()
ar17=open('res_cineasta.txt', 'r')#.read().split()
ar18=open('res_cnte.txt', 'r')#.read().split()
ar19=open('res_mov_autodef.txt', 'r')#.read().split()
ar20=open('res_desaloja_zoc.txt', 'r')#.read().split()
ar21=open('res_detiene_poli.txt', 'r')#.read().split()
ar22=open('res_esp_recomineda.txt', 'r')#.read().split()
ar23=open('res_homb_muerto.txt', 'r')#.read().split()
ar24=open('res_ing_mex.txt', 'r')#.read().split()
ar25=open('res_alain_delon.txt', 'r')#.read().split()
ar26=open('res_alerta_mex.txt', 'r')#.read().split()
ar27=open('res_cae_de_bici.txt', 'r')#.read().split()
ar28=open('res_chapo_rico.txt', 'r')#.read().split()
ar29=open('res_cineasta.txt', 'r')#.read().split()
ar30=open('res_cnte.txt', 'r')#.read().split()
ar31=open('res_mov_autodef.txt', 'r')#.read().split()
ar32=open('res_desaloja_zoc.txt', 'r')#.read().split()
ar33=open('res_detiene_poli.txt', 'r')#.read().split()
ar34=open('res_esp_recomineda.txt', 'r')#.read().split()
ar35=open('res_homb_muerto.txt', 'r')#.read().split()
ar36=open('res_ing_mex.txt', 'r')#.read().split()
ar37=open('res_alain_delon.txt', 'r')#.read().split()
ar38=open('res_alerta_mex.txt', 'r')#.read().split()
ar39=open('res_cae_de_bici.txt', 'r')#.read().split()
ar40=open('res_chapo_rico.txt', 'r')#.read().split()
ar41=open('res_cineasta.txt', 'r')#.read().split()
ar42=open('res_cnte.txt', 'r')#.read().split()
ar43=open('res_mov_autodef.txt', 'r')#.read().split()
ar44=open('res_desaloja_zoc.txt', 'r')#.read().split()
ar45=open('res_detiene_poli.txt', 'r')#.read().split()
ar46=open('res_esp_recomineda.txt', 'r')#.read().split()
ar47=open('res_homb_muerto.txt', 'r')#.read().split()
ar48=open('res_ing_mex.txt', 'r')#.read().split()
ar49=open('res_homb_muerto.txt', 'r')#.read().split()
ar50=open('res_ing_mex.txt', 'r')#.read().split()
#Las palabras separadas por comas se asignan a una lista
ResultadoDoc1 = [line.split() for line in ar1.readlines()]
ResultadoDoc2 = [line.split() for line in ar2.readlines()]
ResultadoDoc3 = [line.split() for line in ar3.readlines()]
ResultadoDoc4 = [line.split() for line in ar4.readlines()]
ResultadoDoc5 = [line.split() for line in ar5.readlines()]
ResultadoDoc6 = [line.split() for line in ar6.readlines()]
ResultadoDoc7 = [line.split() for line in ar7.readlines()]
ResultadoDoc8 = [line.split() for line in ar8.readlines()]
ResultadoDoc9 = [line.split() for line in ar9.readlines()]
ResultadoDoc10 = [line.split() for line in ar10.readlines()]
ResultadoDoc11 = [line.split() for line in ar11.readlines()]
ResultadoDoc12 = [line.split() for line in ar12.readlines()]
ResultadoDoc13 = [line.split() for line in ar1.readlines()]
ResultadoDoc14 = [line.split() for line in ar2.readlines()]
ResultadoDoc15 = [line.split() for line in ar3.readlines()]
ResultadoDoc16 = [line.split() for line in ar4.readlines()]
ResultadoDoc17 = [line.split() for line in ar5.readlines()]
ResultadoDoc18 = [line.split() for line in ar6.readlines()]
ResultadoDoc19 = [line.split() for line in ar7.readlines()]
ResultadoDoc20 = [line.split() for line in ar8.readlines()]
ResultadoDoc21 = [line.split() for line in ar9.readlines()]
ResultadoDoc22 = [line.split() for line in ar10.readlines()]
ResultadoDoc23 = [line.split() for line in ar11.readlines()]
ResultadoDoc24 = [line.split() for line in ar12.readlines()]
ResultadoDoc25 = [line.split() for line in ar1.readlines()]
ResultadoDoc26 = [line.split() for line in ar2.readlines()]
ResultadoDoc27 = [line.split() for line in ar3.readlines()]
ResultadoDoc28 = [line.split() for line in ar4.readlines()]
ResultadoDoc29 = [line.split() for line in ar5.readlines()]
ResultadoDoc30 = [line.split() for line in ar6.readlines()]
ResultadoDoc31 = [line.split() for line in ar7.readlines()]
ResultadoDoc32 = [line.split() for line in ar8.readlines()]
ResultadoDoc33 = [line.split() for line in ar9.readlines()]
ResultadoDoc34 = [line.split() for line in ar10.readlines()]
ResultadoDoc35 = [line.split() for line in ar11.readlines()]
ResultadoDoc36 = [line.split() for line in ar12.readlines()]
ResultadoDoc37 = [line.split() for line in ar1.readlines()]
ResultadoDoc38 = [line.split() for line in ar2.readlines()]
ResultadoDoc39 = [line.split() for line in ar3.readlines()]
ResultadoDoc40 = [line.split() for line in ar4.readlines()]
ResultadoDoc41 = [line.split() for line in ar5.readlines()]
ResultadoDoc42 = [line.split() for line in ar6.readlines()]
ResultadoDoc43 = [line.split() for line in ar7.readlines()]
ResultadoDoc44 = [line.split() for line in ar8.readlines()]
ResultadoDoc45 = [line.split() for line in ar9.readlines()]
ResultadoDoc46 = [line.split() for line in ar10.readlines()]
ResultadoDoc47 = [line.split() for line in ar11.readlines()]
ResultadoDoc48 = [line.split() for line in ar12.readlines()]
ResultadoDoc49 = [line.split() for line in ar11.readlines()]
ResultadoDoc50 = [line.split() for line in ar12.readlines()]
#Remueve caracteres indeseables de cada lista generada con las palabras de documentos
# como '"','"','Fe','1'.
signosIndeseables = ['"','"','Fe','1','Fz','Fit','*','+','-','/']
RD1 = [x for x in ResultadoDoc1 if x != signosIndeseables]
rd1 = [x for x in RD1 if x ]

RD2 = [x for x in ResultadoDoc2 if x != signosIndeseables]
rd2 = [x for x in RD2 if x ]

RD3 = [x for x in ResultadoDoc3 if x != signosIndeseables]
rd3 = [x for x in RD3 if x ]

RD4 = [x for x in ResultadoDoc4 if x != signosIndeseables]
rd4 = [x for x in RD4 if x ]

RD5 = [x for x in ResultadoDoc5 if x != signosIndeseables]
rd5 = [x for x in RD5 if x ]

RD6 = [x for x in ResultadoDoc6 if x != signosIndeseables]
rd6 = [x for x in RD6 if x ]

RD7 = [x for x in ResultadoDoc7 if x != signosIndeseables]
rd7 = [x for x in RD7 if x ]

RD8 = [x for x in ResultadoDoc8 if x != signosIndeseables]
rd8 = [x for x in RD8 if x ]

RD9 = [x for x in ResultadoDoc9 if x != signosIndeseables]
rd9 = [x for x in RD9 if x ]

RD10 = [x for x in ResultadoDoc10 if x != signosIndeseables]
rd10 = [x for x in RD10 if x ]

RD11 = [x for x in ResultadoDoc11 if x != signosIndeseables]
rd11 = [x for x in RD11 if x ]

RD12 = [x for x in ResultadoDoc12 if x != signosIndeseables]
rd12 = [x for x in RD12 if x ]

RD13 = [x for x in ResultadoDoc13 if x != signosIndeseables]
rd13 = [x for x in RD13 if x ]

RD14 = [x for x in ResultadoDoc14 if x != signosIndeseables]
rd14 = [x for x in RD14 if x ]

RD15 = [x for x in ResultadoDoc15 if x != signosIndeseables]
rd15 = [x for x in RD15 if x ]

RD16 = [x for x in ResultadoDoc16 if x != signosIndeseables]
rd16 = [x for x in RD16 if x ]

RD17 = [x for x in ResultadoDoc17 if x != signosIndeseables]
rd17 = [x for x in RD17 if x ]

RD18 = [x for x in ResultadoDoc18 if x != signosIndeseables]
rd18 = [x for x in RD18 if x ]

RD19 = [x for x in ResultadoDoc19 if x != signosIndeseables]
rd19 = [x for x in RD19 if x ]

RD20 = [x for x in ResultadoDoc20 if x != signosIndeseables]
rd20 = [x for x in RD20 if x ]

RD21 = [x for x in ResultadoDoc21 if x != signosIndeseables]
rd21 = [x for x in RD21 if x ]

RD22 = [x for x in ResultadoDoc22 if x != signosIndeseables]
rd22 = [x for x in RD22 if x ]

RD23 = [x for x in ResultadoDoc23 if x != signosIndeseables]
rd23 = [x for x in RD23 if x ]

RD24 = [x for x in ResultadoDoc24 if x != signosIndeseables]
rd24 = [x for x in RD24 if x ]

RD25 = [x for x in ResultadoDoc25 if x != signosIndeseables]
rd25 = [x for x in RD25 if x ]

RD26 = [x for x in ResultadoDoc26 if x != signosIndeseables]
rd26 = [x for x in RD26 if x ]

RD27 = [x for x in ResultadoDoc27 if x != signosIndeseables]
rd27 = [x for x in RD27 if x ]

RD28 = [x for x in ResultadoDoc28 if x != signosIndeseables]
rd28 = [x for x in RD28 if x ]

RD29 = [x for x in ResultadoDoc29 if x != signosIndeseables]
rd29 = [x for x in RD29 if x ]

RD30 = [x for x in ResultadoDoc30 if x != signosIndeseables]
rd30 = [x for x in RD30 if x ]

RD31 = [x for x in ResultadoDoc31 if x != signosIndeseables]
rd31 = [x for x in RD31 if x ]

RD32 = [x for x in ResultadoDoc32 if x != signosIndeseables]
rd32 = [x for x in RD32 if x ]

RD33 = [x for x in ResultadoDoc33 if x != signosIndeseables]
rd33 = [x for x in RD33 if x ]

RD34 = [x for x in ResultadoDoc34 if x != signosIndeseables]
rd34 = [x for x in RD34 if x ]

RD35 = [x for x in ResultadoDoc35 if x != signosIndeseables]
rd35 = [x for x in RD35 if x ]

RD36 = [x for x in ResultadoDoc36 if x != signosIndeseables]
rd36 = [x for x in RD36 if x ]

RD37 = [x for x in ResultadoDoc37 if x != signosIndeseables]
rd37 = [x for x in RD37 if x ]

RD38 = [x for x in ResultadoDoc38 if x != signosIndeseables]
rd38 = [x for x in RD38 if x ]

RD39 = [x for x in ResultadoDoc39 if x != signosIndeseables]
rd39 = [x for x in RD39 if x ]

RD40 = [x for x in ResultadoDoc40 if x != signosIndeseables]
rd40 = [x for x in RD40 if x ]

RD41 = [x for x in ResultadoDoc41 if x != signosIndeseables]
rd41 = [x for x in RD41 if x ]

RD42 = [x for x in ResultadoDoc42 if x != signosIndeseables]
rd42 = [x for x in RD42 if x ]

RD43 = [x for x in ResultadoDoc43 if x != signosIndeseables]
rd43 = [x for x in RD42 if x ]

RD44 = [x for x in ResultadoDoc44 if x != signosIndeseables]
rd44 = [x for x in RD44 if x ]

RD45 = [x for x in ResultadoDoc45 if x != signosIndeseables]
rd45 = [x for x in RD45 if x ]

RD46 = [x for x in ResultadoDoc46 if x != signosIndeseables]
rd46 = [x for x in RD46 if x ]

RD47 = [x for x in ResultadoDoc47 if x != signosIndeseables]
rd47 = [x for x in RD47 if x ]

RD48 = [x for x in ResultadoDoc48 if x != signosIndeseables]
rd48 = [x for x in RD48 if x ]

RD49 = [x for x in ResultadoDoc49 if x != signosIndeseables]
rd49 = [x for x in RD49 if x ]

RD50 = [x for x in ResultadoDoc50 if x != signosIndeseables]
rd50 = [x for x in RD50 if x ]

##print 'Contenido de documento rd1'
##print(rd1)
##print 'Contenido de documento rd2'
##print(rd2)
##print 'Contenido de documento consulta'
##print(consulta)


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
    cont = 0
    for item in lista:
        if item[2] in eagles_dict.keys():
            listaPalabras.append([item[1],item[2]])
            res = collections.Counter(map(tuple, listaPalabras))
            result =[[key[0], key[1], value] for key, value in res.iteritems()]
            #result = [(k,v,i) for (k,v) in res]
                
            
    return result
################################

#Función que toma el número de palabras de la lista y regresa una lista con esos
#números

##def vectores(doc1, doc2, consulta):
##    lista = doc1 + doc2 + consulta
##    result1 = [0] * len(lista)
##    result2 = [0] * len(lista)
##    result3 = [0] * len(lista)
##    for index,value in enumerate([ item[2] for item in doc1 ]):
##        result1[index] = value
##    for index,value in enumerate([ item[2] for item in doc2 ]):
##        result2[index] = value
##    for index,value in enumerate([ item[2] for item in consulta ]):
##        result3[index] = value
##
##    return result1,result2,result3

def vector(doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10,\
            doc11, doc12, doc13, doc14, doc15, doc16, doc17, doc18, doc19,\
            doc20, doc21, doc22, doc23, doc24, doc25, doc26, doc27, doc28,\
            doc29, doc30, doc31, doc32, doc33, doc34, doc35, doc36, doc37,\
            doc38, doc39, doc40, doc41, doc42, doc43, doc44, doc45, doc46,\
            doc47, doc48, doc49, doc50, l):
    lista = doc1 + doc2 + doc3 + doc4 + doc5 + doc6 + doc7 + doc8 + doc9 + \
            doc10 + doc11 + doc12 + doc13 + doc14 + doc15 + doc16 + doc17 + \
            doc18 + doc19 + doc20 + doc21 + doc22 + doc23 + doc24 + doc25 +\
            doc26 + doc27 + doc28 + doc29 + doc14 + doc30 + doc31 + doc32 + \
            doc33 + doc34 + doc35 + doc36 + doc37 + doc38 + doc39 + doc40 +\
            doc41 + doc42 + doc43 + doc44 + doc45 + doc46 + doc47 + doc48 + \
            doc49 + doc50
    result = [0] * len(lista)
    for index,value in enumerate([ item[2] for item in l ]):
        result[index] = value
    return result


##1st attempt
##def vectores(doc1,doc2,consulta):
##    res1=[]
##    res2=[]
##    res3=[]
##    l1=[]
##    cont = 0
##    r = doc1 + doc2 + consulta
##    for i in r:
##        l1.append(i[0])
##        res1.append(0)
##        res2.append(0)
##        res3.append(0)
##    for e in doc1:
##        if e[0] in l1:
##            res1.append(e[2])
##        else:
##            if e[0] not in l1:
##                res1.popleft(0))
##    for e in doc2:
##        if e[0] in l1:
##            res2.append(e[2])
##        else:
##            if e[0] not in l1:
##                res2.popleft(0)
##    for e in consulta:
##        if e[0] in l1:
##            res3.append(e[2])
##        else:
##            if e[0] not in l1:
##                res3.popleft(0)
##    return len(l1),len(res1)
##    
##    #result = [1 if doc1 in r else 0 for doc1 in r]
##    #result = [x in doc1 for x in r]
##    kset = set(tuple(x) for x in r)
##    result = [tuple(x) in kset for x in r]
    #return result
###############################            
def tfidf(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,\
          v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,\
          v21, v22, v23, v24, v25, v26, v27, v28, v29, v30,\
          v31, v32, v33, v34, v35, v36, v37, v38, v39, v40,\
          v41, v42, v43, v44, v45, v46, v47, v48, v49, v50):
    v = [v1, v2, v2, v3, v4, v5, v6, v7, v8, v9, v10,\
          v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,\
          v21, v22, v23, v24, v25, v26, v27, v28, v29, v30,\
          v31, v32, v33, v34, v35, v36, v37, v38, v39, v40,\
          v41, v42, v43, v44, v45, v46, v47, v48, v49, v50]
    countdict = {}
    for vi in v:
        for e in vi:
            countdict[e[0]] = countdict.get(e[0],0) + 1

    scoredict = {}
    for vi in v:
        for e in vi:
            scoredict[e[0]] = scoredict.get(e[0],0) + (e[2] * math.log10(3.0/countdict[e[0]]))

    return scoredict

def normalizing(dic, doc1):
    result = []
    for letter in dic:
        for element in doc1:
            if letter in element:
                result.append(dic[letter]**2)
    return math.sqrt(sum(result))
        
    
##def normalizing(dic, l1):
##    result = []      
##    for i in dic:
##        if any(i in row for row in l1):
##            result.append(dic[i]) 
##    return norm(result)

##
##def normalizing(dic, l):
##    result = []
##    for i in dic:
##        if i in [j[0] for j in l]:
##            result.append(dic[i])
##
##    print result #[0.4, 0.1, 0.2]
##    return math.sqrt(sum(k*k for k in result))
################################
##def f1(doc1, doc2, consulta):
##    lista_docs = []
##    listapalabrasDoc1 =[]
##    lista_docs = ['doc1', 'doc2', 'consulta']
##    for item in doc1:
##        if item[2] in eagles_dict.keys():
##            listapalabrasDoc1.append(item[1])
##    for i in listapalabrasDoc1:
##            resultDoc1 = tf_idf(i, doc1, lista_docs)
##    return resultDoc1
##                                     
##def f2(doc1, doc2, consulta):
##    lista_docs = []
##    listapalabrasDoc2 =[]
##    lista_docs = ['doc1', 'doc2', 'consulta']
##    #print(lista_docs)
##    for item in doc2:
##        if item[2] in eagles_dict.keys():
##            listapalabrasDoc2.append([item[1])
##    for i in listapalabrasDoc2:
##        resultDoc2 = tf_idf(i, doc2, lista_docs)
##    return resultDoc2
##                                     
##def f3(doc1, doc2, consulta):
##    lista_docs = []
##    listapalabrasConsulta =[]
##    lista_docs = ['doc1', 'doc2', 'consulta']
##    #print(lista_docs)
##    for item in consulta:
##        if item[2] in eagles_dict.keys():
##            listapalabrasConsulta.append([item[1])
##    for i in listapalabrasConsulta:
##        resultDoc2 = tf_idf(i, doc2, lista_docs)
##    return resultConsulta

################################
##print "DOCUMENTO 1"
##print(compara(rd1))
##print "DOCUMENTO 2"
##print(compara(rd2))
##print "CONSLUTA"
##print(compara(consulta))
##print '################################'
##################################
##print "VECTORES DOCUMENTO 1 "
##print(vector1(compara(rd1),compara(rd2),compara(consulta)))
##print "VECTORES DOCUMENTO 2 "
##print(vector2(compara(rd1),compara(rd2),compara(consulta)))
##print "VECTORES DOCUMENTO Consulta "
##print(vectorConsulta(compara(rd1),compara(rd2),compara(consulta)))
##print '################################'
##################################
##print "DOCUMENTO 1"
##print(compara(rd1))
##print "DOCUMENTO 2"
##print(compara(rd2))
##print "CONSLUTA"
##print(compara(consulta))
##print '################################'
##################################
##print 'tf idf' 
##print(tfidf(compara(rd1),compara(rd2),compara(consulta)))
#print '################################'
#print 'tf idf' 
#print(tfidf2(vector1(compara(rd1),compara(rd2),compara(consulta)),vector2(compara(rd1),compara(rd2),compara(consulta)),vectorConsulta(compara(rd1),compara(rd2),compara(consulta))))
print '################################'
print 'valores normalizados'
print 'normalizacion documento 1'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd1)))
print 'normalizacion documento 2'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd2)))
print 'normalizacion documento 3'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd3)))
print 'normalizacion documento 4'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd4)))
print 'normalizacion documento 5'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd5)))
print 'normalizacion documento 6'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd6)))
print 'normalizacion documento 7'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd7)))
print 'normalizacion documento 8'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd8)))
print 'normalizacion documento 9'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd9)))
print 'normalizacion documento 10'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd10)))
print 'normalizacion documento 11'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd11)))
print 'normalizacion documento 12'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd12)))
print 'normalizacion documento 13'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd13)))
print 'normalizacion documento 14'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd14)))
print 'normalizacion documento 15'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd15)))
print 'normalizacion documento 16'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd16)))
print 'normalizacion documento 17'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd17)))
print 'normalizacion documento 18'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd18)))
print 'normalizacion documento 19'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd19)))
print 'normalizacion documento 20'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd20)))
print 'normalizacion documento 21'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd21)))
print 'normalizacion documento 22'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd22)))
print 'normalizacion documento 23'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd23)))
print 'normalizacion documento 24'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd24)))

print 'normalizacion documento 25'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd25)))
print 'normalizacion documento 26'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd26)))
print 'normalizacion documento 27'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd27)))
print 'normalizacion documento 28'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd28)))
print 'normalizacion documento 29'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd29)))
print 'normalizacion documento 30'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd30)))
print 'normalizacion documento 31'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd31)))
print 'normalizacion documento 32'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd32)))
print 'normalizacion documento 33'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd33)))
print 'normalizacion documento 34'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd34)))
print 'normalizacion documento 35'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd35)))
print 'normalizacion documento 36'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd36)))
print 'normalizacion documento 37'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd37)))
print 'normalizacion documento 38'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd38)))
print 'normalizacion documento 39'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd39)))
print 'normalizacion documento 40'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd40)))
print 'normalizacion documento 41'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd41)))
print 'normalizacion documento 42'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd42)))
print 'normalizacion documento 43'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd43)))

print 'normalizacion documento 44'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd44)))
print 'normalizacion documento 45'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd45)))
print 'normalizacion documento 46'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd46)))
print 'normalizacion documento 47'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd47)))
print 'normalizacion documento 48'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd48)))
print 'normalizacion documento 49'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd49)))
print 'normalizacion documento 50'
print (normalizing(tfidf(compara(rd1),compara(rd2),compara(rd3),compara(rd4)\
                         ,compara(rd5),compara(rd6),compara(rd7),compara(rd8)\
                         ,compara(rd9),compara(rd10),compara(rd11),compara(rd12)\
                         ,compara(rd13),compara(rd14),compara(rd15),compara(rd16)\
                         ,compara(rd17),compara(rd18),compara(rd19),compara(rd20)\
                         ,compara(rd21),compara(rd22),compara(rd23),compara(rd24)\
                         ,compara(rd25),compara(rd26),compara(rd27),compara(rd28)\
                         ,compara(rd29),compara(rd30),compara(rd31),compara(rd32)\
                         ,compara(rd33),compara(rd34),compara(rd35),compara(rd36)\
                         ,compara(rd37),compara(rd38),compara(rd39),compara(rd40)\
                         ,compara(rd41),compara(rd42),compara(rd43),compara(rd44)\
                         ,compara(rd45),compara(rd46),compara(rd47),compara(rd48)\
                         ,compara(rd49),compara(rd50)),compara(rd50)))

##print ''            
##print'Prueba de f1 '
##print(f1(rd1,rd2,consulta))
##print ''

##print ''            
##print'Prueba de f2 '
##print(f1(rd1,rd2,consulta))
##print ''
##
##print ''            
##print'Prueba de f1 '
##print(f1(rd1,rd2,consulta))
##print '' 

################################


################################
##print "VECTORES DOCUMENTO "
##print(vectores(compara(rd1),compara(rd2),compara(consulta)))
##print "VECTORES DOCUMENTO 1"
##print(vectores(compara(rd1)))
##print "VECTORES DOCUMENTO 2"
##print(vectores(compara(rd2)))
##print "VECTORES CONSULTA"
##print(vectores(compara(consulta)))

##################################
##
##print "RESULTADO DOCUMENTO 1"
##print(coseno(vectores(compara(rd1)),vectores(compara(consulta))))
##
##print "RESULTADO DOCUMENTO 2"
##print(coseno(vectores(compara(rd2)),vectores(compara(consulta))))
###Nota: Hasta ahora el programa no compila porque para que el producto interno
###de vectores se cumpla, necesita tener el mismo número de elementos
##
##def frecuencia(palabra, doc):
##    return doc.count(palabra)
## 
## 
##def cuenta_palabras(doc):
##    return len(doc)
## 
## 
##def tf(palabra, doc):
##    return (frecuencia(palabra, doc) / float(cuenta_palabras(doc)))
## 
## 
##def num_docs_contiene(palabra, lista_de_docs):
##    contador = 0
##    for document in lista_de_docs:
##        if frecuencia(palabra, document) > 0:
##            contador += 1
##    return 1 + contador
## 
## 
##def idf(palabra, lista_de_docs):
##    return math.log(len(lista_de_docs) /
##            float(num_docs_contiene(palabra, lista_de_docs)))
## 
## 
##def tf_idf(palabra, doc, lista_de_docs):
##    return (tf(palabra, doc) * idf(palabra, lista_de_docs))        
    
       



