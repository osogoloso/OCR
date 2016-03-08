# -*- coding: utf-8 -*-
"""
@author: Ivan B & Donaldo
"""
# Se importan librerias
import os    #nos permite acceder a funcionalidades dependientes del Sistema Operativo
import matplotlib.image as mpimg #libreria para el tratamiento de iamgenes matplotlib sólo admite imágenes PNG.
import csv #libreria para el manejo de archivos CSV (de Valores Separados por Comas)
import math
import operator


# Parametros: Ninguno
# Descripcion: en esta funcion se leen las carpetas contenidas en la carpeta "0-9/"
#   y dentro de cada una de las carpetas se lee cada una de las imagenes. 
#   Al leer la imagen se le aplican las 14 funciones para extraer ciertas 
#   propiedas de dicha imagen. Todos los datos que se extraen de cada imagen se 
#   guardan en un arreglo. Para finalizar los datos del arreglo se guardan en un 
#   archivo .csv
#Variables de retorno: Ninguno
def abrirImagen():
    arreglo=[] #Se crea el arreglo para guardar los datos de cada imagen  
    print (">>Creando DATASET...")#impresion en pantalla 
    for x in range(0,10): # for para recorrer cada carpeta
        clase=x #indica el nombre de la clase
        print (" Extrayendo datos- - - - -> Clase:",clase)#impresion en pantalla de las clases que se estan leyendo
        print ("**",clase)#impresion de pantalla de la clase que se esta leyendo 

        direc="0-9/"+str(clase)+"/" #ubicación de las carpetas del 0-9
        
        #numero de imagenes que contiene la carpeta
        imagenes=directory("0-9/"+str(clase))
        j=0#contador que representa el nombre de la imagen
        for i in range(0,imagenes): #for para recorrer cada imagen
            j1 = "%03d" % j  # convertir los numeros en cifras de 3 digitos ej: 1-->001
            temp = os.path.exists(direc+str(clase)+"_"+str(j1)+".png")#regresa true en caso
            #de que exista el nombre del archivo o false de  no existir.
            
            #comprobar que la imagen existe dentro de la carpeta, 
            #mientras no exista el nombre de la imagen 
            #seguira avanzando hasta encontrar
            while not(temp):
                j+=1 #contador que incrementa a 1
                j1 = "%03d" % j #convertir los numeros en cifras de 3 digitos ej: 1-->001
                temp = os.path.exists(direc+str(clase)+"_"+str(j1)+".png")#regresa true en caso
            #de que exista el nombre del archivo o false de  no existir.
            #se rompe el ciclo while
            if (os.path.exists(direc+str(clase)+"_"+str(j1)+".png")):#se confirma una vez mas que
            #la imagen existe, para la extraccion de atributos
            
                print (direc+str(clase)+"_"+str(j1)+".png")
                
                #Valores de Atributos 0-14#
                img=mpimg.imread(direc+str(clase)+"_"+str(j1)+".png")#Leer la imagen
                vp1=p1(img)  #Propiedad 1: #columnas/#filas 
                vp2=p2(img) #Propiedad 2:  #1's/ tamaño total de la imagen  
                vp3=p3(img) #Propiedad 3:#1's/columnas en la #fila/2
                vp4=p4(img) #Propiedad 4:#1's/columnas en la #fila/4
                vp5=p5(img) #Propiedad 5:#1's/columnas en la 3(#fila/4)
                vp6=p6(img) #Propiedad 6:#1's/filas en la #columnas/2
                vp7=p7(img) #Propiedad 7:#1's/filas en la #columnas/4
                vp8=p8(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp9=p9(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp10=p10(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp11=p11(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp12=p12(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp13=p13(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                vp14=p14(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
                      
                #se concatenan todos los valores de cada imagen separados por una coma
                linea=str(vp1)+","+str(vp2)+","+str(vp3)+","+str(vp4)+","+str(vp5)+","+str(vp6)+","+str(vp7)+","+str(vp8)+","+str(vp9)+","+str(vp10)+","+str(vp11)+","+str(vp12)+","+str(vp13)+","+str(vp14)+","+str(clase)
                
                #Se agrega la linea con los datos de cada imagen en el arreglo
                arreglo.append(linea)#agregar una linea

                j+=1#contador con incremento en 1 (recorre imagenes)
    #se pasa el arreglo como parametro de entrada para pasar los datos a un archivo csv
    archivoCSV(arreglo)
    print ("\n>> DATASET CREADO CON EXITO <<")

        


#Parametros: una imagen iterable
#Descripcion: se realiza la siguiente operacion: No.filas/No.columnas
#Variables de retorno: pro1 que es un numero decimal  (el resultado de NoFilas/NoColumnas)
def p1(imagen):
    filas=len(imagen[:,0]) #Total de filas de la imagen
    col=len(imagen[0,:])   #Total de columnas de la imagen
    pro1=filas/col #razon total= #filas/#columnas
    return pro1 #regresa el valor de pro1


#Parametros: una imagen iterable
#Descripcion: Calcula cuantos 1's existen en toda la imagen y este resultado 
#se divide sobre el tamaño total de la imagen (No. 1's/tamaño de la imagen)
#Variables de retorno: con1 que es un numero decimal (el resultado de No.1's/(filas*col) )
def p2(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    for i in range(0,filas): #recorre las filas de la imagen
        for j in range(0,col): #recorre las columnas de la imagen
            if(imagen[i,j]==1): #si encuentra un 1...
                con1=con1+1 #contador de 1's aumentará uno mas
    con1=con1/(filas*col)#total de unos divido entre el total de la imagen(filas/columnas)
    return con1#retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula cuantos 1's existen en la fila que se encuentra a la mitad 
#   de la imagen y este resultado se divide sobre el numero total de columnas 
#Variables de retorno: con1 que es un numero
def p3(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen  
    mitad=int(filas/2) #escoge la fila que esta a la mitad de la imagen
    for i in imagen[int(mitad),:]: #recorre en la fila quese encuentra a la mitad de la imagen
        if(i==1): #si encuentra un 1...
            con1=con1+1 #el contador aumentará uno mas
    #el numero de 1's encontrados en la fila se divide entre el total de columnas
    con1=con1/col 
    return con1#retorna a con1


#Parametros: una imagen iterable
#Descripcion:  Calcula cuantos 1's existen en la fila que se encuentra en la cuarta 
#parte de la imagen y este resultado se divide sobre el numero total de columnas 
#Variables de retorno: con1 es un numero, es el resultado de No.1'/No.Columnas
def p4(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    cuarto=int(filas/4)    #escoge la imagen que se encuentra a un cuarto de la imagen
    for i in imagen[int(cuarto),:]: #recorre la fila que se encuentra en un cuarto de la imagen
        if(i==1): #si encuentra un 1 
            con1=con1+1#el contador de unos incrementara 1
    #el numero de 1's encontrados en la fila se divide entre el total de columnas
    con1=con1/col
    return con1# retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula cuantos 1's existen en la fila que se encuentra a tres cuartas
#partes de la imagen y este resultado se divide sobre el numero total de columnas
#Variables de retorno: con1 es un numero, es el resultado de No.1'/No.Columnas
def p5(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    cuarto=int(3*(filas/4))      #Define la fila que se va a usar
    for i in imagen[cuarto,:]:#recorre la fila que se encuentra a tres cuartos de la imagen
        if(i==1):#si encuentra un 1
            con1=con1+1#incrementa el contador a 1
    ##el numero de 1's encontrados en la fila se divide entre el total de columnas
    con1=con1/col
    return con1#retorna a con1


#Parametros: una imagen iterable
#Descripcion: Calcula cuantos 1's existen en la columna que se encuentra a la mitad de 
#   la imagen y este resultado se divide sobre el numero total de filas
#Variables de retorno: con1 es un numero, es el resultado de No.1'/No.Filas
def p6(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    mitad=int(col/2) #define la columna que se encuentra a la mitad de la imagen
    for i in imagen[:,mitad]:#recorre la columna que se encuentra a la mitad de la imagen
        if(i==1):#si encuentra un 1
            con1=con1+1#incrementa el contador a 1
    #el numero de 1's encontrados en la columna se divide entre el total de filas
    con1=con1/filas
    return con1#retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion:  Calcula cuantos 1's existen en la columna que se encuentra en la cuarta
#   parte de la imagen y este resultado se divide sobre el numero total de filas
#Variables de retorno: con1 es un numero, es el resultado de No.1'/No.Filas
def p7(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    cuarto=int(col/4)#define la columna que se encuentra a un cuarto de la imagen
    for i in imagen[:,cuarto]:#recorre la columna que se encuentra a tres cuarts partes de la imagen
        if(i==1):#si encuentra un 1
            con1=con1+1#incrementa el contador en 1
    #el numero de 1's encontrados en la columna se divide entre el total de filas            
    con1=con1/filas
    return con1#retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula cuantos 1's existen en la columna que se encuentra a tres cuartas
#   partes de la imagen y este resultado se divide sobre el numero total de filas
#Variables de retorno: con1 es un numero, es el resultado de No.1'/No.Filas
def p8(imagen):
    con1=0#contador de 1's
    col=len(imagen[0,:])  #total de filas de la imagen
    filas=len(imagen[:,0])#total de columnas de la imagen
    cuarto3=int(3*col/4)#define la columna que se encuentra a tres cuartas partes de la imagen
    for i in imagen[:,cuarto3]:#recorre la columna que se encuentra a tres cuartas partes de la img.
        if(i==1):#si encuentra un 1
            con1=con1+1#incrementa el contador en 1
    #el numero de 1's encontrados en la columna se divide entre el total de filas     
    con1=con1/filas
    return con1#retorna en con1


#Parametros: una imagen iterable
#Descripcion: Calcula el numero de cortes en la mitad de las filas de una imagen,
# es decir, el numero de cambios de 0 a 1  que existen
#Variables de retorno: con1 es un numero, es el No.Cortes
def p9(imagen):
    con1=0 #contador de 1's 
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])   #Total de columnas de la imagen
    mitad=int(filas/2)    #define la fila que se encuentra a la mitad de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[mitad,:])-1): #recorre la fila seleccionada
        x=imagen[mitad,h]#indica la posicion presente 
        j=h+1#indica el incremento de la posicion presente de h
        y=imagen[mitad,j]#posicion futura
        #print ("con1",con1)                        
        if(y!=x): #compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        #print ("h",h)
        h+=1#incremento de h
    if imagen[mitad,0]==1:#indica el cambio al inicio de la imagen
            con1+=1 #incrementa a uno si existe cambio
    if  imagen[mitad,(col-1)]==1:#indica el cambio al final de la imagen
            con1+=1#increenta a uno si existe cambio
    return con1 #retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula el numero de cortes en la cuarta parte del numero de filas 
#   de una imagen,es decir, el numero de cambios de 0 a 1  que existen.
#Variables de retorno: con1 es un numero, es el No.Cortes
def p10(imagen):
    con1=0 #contador de cortes
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    cuarto=int(filas/4)#define la fila que se encuentra a una cuarta parte de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[cuarto,:])-1):#recorre la fila seleccionada
        x=imagen[cuarto,h]#indica la posicion presente
        j=h+1#indica el incremento de la posicion presente de h
        y=imagen[cuarto,j]#posicion futura
        
        if(x!=y): #compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        h+=1#incremento de h
    if imagen[cuarto,0]==1:#indica el cambio al inicio de la imagen
            con1+=1#incrementa a uno si existe cambio
    if  imagen[cuarto,(col-1)]==1:#indica el cambio al final de la imagen
            con1+=1#increenta a uno si existe cambio
    return con1#retorna el valor de con1


#Parametros: una imagen iterable 
#Descripcion: Calcula el numero de cortes en tres cuartas partes de las filas 
#de una imagen,es decir, el numero de cambios de 0 a 1  que existen
#Variables de retorno: con1 es un numero, es el No.Cortes
def p11(imagen):
    con1=0 #contador de cortes
    filas=len(imagen[:,0])  #Total de filas de la imagen
    col=len(imagen[0,:])    #Total de columnas de la imagen
    cuarto=int(3*(filas/4))#define la fila que se encuentra a tres cuartas partes de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[cuarto,:])-1):#recorre la fila seleccionada
        x=imagen[cuarto,h]#indica la posicion presente
        j=h+1#indica el incremento 
        y=imagen[cuarto,j]#posicion futura
        if(x!=y):#compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        h+=1#incremento de h
    if imagen[cuarto,0]==1:#indica el cambio al inicio de la imagen
            con1+=1#incementa a uno si existe el cambio
    if  imagen[cuarto,(col-1)]==1:#indica el cambio al final de la imagen
            con1+=1#incrementa a uno si existe cambio
    return con1#retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula el numero de cortes en la mitad de las columnas de una imagen,
#   es decir, el numero de cambios de 0 a 1  que existen
#Variables de retorno: con1 es un numero, es el No.Cortes
def p12(imagen):
    con1=0 #contador de cortes
    col=len(imagen[0,:])    #Total de columnas de la imagen
    filas=len(imagen[:,0])  #Total de filas de la imagen
    mitad=int(col/2)#define el numero de columnas que se encuentra a la mitad de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[:,mitad])-1):#recorre la columna seleccionada
        x=imagen[h,mitad]#indica la posicion presente
        j=h+1#indica el incremento
        y=imagen[j,mitad]#posicion futura
        if(x!=y):#compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        h+=1#incremento de h
    if imagen[0,mitad]==1:#indica el cambio al inicio de la imagen
            con1+=1#incementa a uno si existe el cambio
    if  imagen[(filas-1),mitad]==1:#indica el cambio al final de la imagen
            con1+=1#incementa a uno si existe el cambio
    
    return con1#retorna el valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula el numero de cortes en una cuarta parte de las columnas 
#   de una imagen,es decir, el numero de cambios de 0 a 1  que existen
#Variables de retorno: con1 es un numero, es el No.Cortes
def p13(imagen):
    con1=0 #contador de cortes
    col=len(imagen[0,:])    #Total de columnas de la imagen
    filas=len(imagen[:,0])  #Total de filas de la imagen
    cuarto=int(col/4)#define el numero de columnas que se encuentra a un cuarto de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[:,cuarto])-1):#recorre la columna seleccionada
        x=imagen[h,cuarto]#indica la posicion presente
        j=h+1#indica el incremento
        y=imagen[j,cuarto]#posicion futura
        
        if(x!=y):#compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        h+=1#incremento de h
    if imagen[0,cuarto]==1:#indica el cambio al inicio de la imagen
            con1+=1#incementa a uno si existe el cambio
    if  imagen[(filas-1),cuarto]==1:#indica el cambio al final de la imagen
            con1+=1#incementa a uno si existe el cambio
    return con1#retorna al valor de con1


#Parametros: una imagen iterable
#Descripcion: Calcula el numero de cortes en tres cuartas partes de las columnas 
#   de una imagen,es decir, el numero de cambios de 0 a 1  que existen
#Variables de retorno: con1 es un numero, es el No.Cortes
def p14(imagen):
    con1=0 #contador de cortes
    col=len(imagen[0,:])    #Total de columnas de la imagen
    filas=len(imagen[:,0])  #Total de filas de la imagen
    cuarto=int(3*(col/4))#define el numero de columnas que se encuentra a tres cuartos de la imagen
    h=0#el contador se inicializa en 0
    for i in range(len(imagen[:,cuarto])-1):#recorre la columna seleccionada
        x=imagen[h,cuarto]#indica la posicion presente
        j=h+1#indica el incremento
        y=imagen[j,cuarto]#posicion futura
        
        if(x!=y):#compara el contenido de las posiciones
            con1+=1#incrementa el contador de unos
        h+=1#incremento de h
    if imagen[0,cuarto]==1:#indica el cambio al inicio de la imagen
            con1+=1#incrementa a uno si existe el cambio
    if  imagen[(filas-1),cuarto]==1:#indica el cambio al final de la imagen
            con1+=1#incrementa a uno si existe el cambio
    return con1#retorno al valor de con1



#Parametros: direccion de la ubicacion de una carpeta
#Descripcion: contabilza cuantos archivos existen dentro de una carpeta
#Variables de retorno: conta es el total de archivos que existen en una carpeta
def directory(direc):
  lista = [] #Declarar arreglo para guardar el nombre de los archivos existentes en una carpeta
  lista = os.listdir(direc) #Agrega al arreglo la lista de archivos
  conta = 0 #Contador para el número de archivos
  for i in lista:#Recorre el arreglo lista
      conta += 1 #incrementa a 1
  return conta #retorna a la variable conta


#Parametros: un arreglo 
#Descripcion: con los datos del arreglo de entrada se crea un archivo CSV.
#   El archivo .CSV se guarda en la carpeta en donde se encuentra el programa OCR.py
#Variables de retorno: Ninguno
def archivoCSV(arreglo): #crearo abrir el archivo
    f = open('dataset.csv', 'w')#abrir archivo en caso de existir, de lo contrario crearlo
    for i in range(len(arreglo)):#el archivo contendra todos los datos del arreglo
        f.write(arreglo[i]+"\n")#escribir dentro del archivo cada elemento del arreglo
    f.close()#cerrar el archivo


#Parametros: Ninguno
#Descripcion: Calcula las distancias de cada uno de los datos menos el atributo que se va a
#   predecir con la siguiente formula euclidiana: (sumatoria(Xi-Xj)**2)^1/2
#Variables de retorno: distancias que es un arreglo dimensional con todas las distancias
def leerCSV(nombre): #recibe el nombre de la imagen
    reader = csv.reader(open('dataset.csv'))#abre el dataset
    distancias=[]#arreglo que guarda los resultados de la formula aplicada
    nuevaA=[]#guarda los valores de la nueva instancia
    nueva=instanciaN(nombre).split(",")#metodo donde se obtienen las caracteristicas de la nueva
    #instancia
    for k in nueva:
        nuevaA.append(k) #llena el arreglo con los valores de la nueva instancia       
    num=0#contador de instancias
    for i in reader:#leer archivo fila por fila
        d=0#
        num+=1#numero de instancias en el dataset, incremeta a 1
        for h in range(len(i)-1):#avanza en cada elemento de la fila
            xi=float(i[h])#representa un elemento de la fila del dataset
            xj=float(nuevaA[h])#representa un elemento de la nueva instancia         
            d+=(xi-xj)**2#suma los valores de la diferencia de cada instancia y los eleva al cuadrado
        dis=math.sqrt(d)#raiz cuadradra de la sumatoria
        distancias.append((num,str(i[14]),dis))#se agrega al arreglo el  numero de la imagen
        #la clase y la distancia final
    return distancias#retorna al arreglo ya lleno


#Parametros: arreglo dimensional de las distancias
#Descripcion: Ordena de menor a mayor el arreglo y solo selecciona los 5 distancias 
#   (vecinos) mas cercanos
#Variables de retorno: vecinos, es el arreglo con los k-vecinos mas cercanos
def menorMayor(arreglo,k):#entrada arreglo de distancias y el valor de K
    listaord=[]#crea el arreglo donde se guarda las distancias de menor a mayor
    listaord = sorted(arreglo, key=operator.itemgetter(2), reverse=False)#funcion ordenar datos
    #que se va a ordenar, aparir de quien se va a ordenar(columna: distancias, como se va a ordenar:
    #menor a mayor
    vecinos=[]#arreglo donde se guardan los vecinos dependiendo del valor de K
    
    for x in range(0,k):#de 0 a cuantos elementos se seleccionaran
        vecinos.append(listaord[x])#se agrega el elemento que se encuentra de 0 a k vecinos
    #print ("vecinos",vecinos)
    return vecinos#retorna el arreglo con los vecinos mas cercanos


#Parametros: Arreglo con los K vecinos mas cercanos
#Descripcion: del arreglo de entrada reliza una votacion sobre las repeticiones de las clases.
#   dice a que clase pertenece la nueva imagen(instancia)
#Variables de retorno: Ninguno
def kvecinos(arreglo):
    uno=0#contador de la clase uno
    dos=0#contador de la clase dos
    tres=0#contador de la clase tres
    cuatro=0#contador de la clase cuatro
    cinco=0#contador de la clase cinco
    seis=0#contador de la clase seis
    siete=0#contador de la clase siete
    ocho=0#contador de la clase ocho
    nueve=0#contador de la clase nuevo
    zero=0#contador de la clase cero
    lista=[]#arreglo donde guardan los contadores anteriores
    
    for x in arreglo:#recorrer el arreglo que entra
        n=int(x[1])#representa un valor del arreglo
        if n==0:#si n es igual a 0 entonces...
            zero+=1#contador de la clase zero incrementa uno
        if n==1:#si n es igual a 1 entonces...
            uno+=1#contador de clase uno incrementa uno
        if n==2:#si n es igual a 2 entonces...
            dos+=1#contador de clase dos incrementa uno
        if n==3:#si n es igual a 3 entonces...
            tres+=1#contador de clase tres incrementa uno
        if n==4:#si n es igual a 4 entonces...
            cuatro+=1#contador de clase cuatro incrementa uno
        if n==5:#si n es igual a 5 entonces...
            cinco+=1#contador de clase cinco incrementa uno
        if n==6:#si n es igual a 6 entonces...
            seis+=1#contador de clase seis incrementa uno
        if n==7:#si n es igual a 7 entonces...
            siete+=1#contador de clase siete incrementa uno
        if n==8:#si n es igual a 8 entonces...
            ocho+=1#contador de clase ocho incrementa uno
        if n==9:#si n es igual a 9 entonces...
            nueve+=1#contador de clase nueve incrementa uno
    lista.append((0,zero))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((1,uno))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((2,dos))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((3,tres))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((4,cuatro))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((5,cinco))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((6,seis))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((7,siete))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((8,ocho))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    lista.append((9,nueve))#agregar el elemento indicado al arreglo: clase y numero de repeticiones
    
    #print (listaord)
    
    return lista#retorna a la lista anterior

#Funcion: listaOrd()
#Parametros: arreglo unidimensional que es la lista de clase y numero de repeticiones
#Descripcion: ordena la lista de repeticiones de mayor a menor, para unicamente mostrar
#   la clase con el mayor numero de repeticiones
#Variables de retorno: ninguno
def listaOrd(lista):#entra lista de repeticiones
    listaord = sorted(lista, key=operator.itemgetter(1), reverse=True)#buscar repeticiones
    #de mayor a menor
    #for i in range(0,1):#saca un elemento del arreglo
    f=listaord[0]#saca el elemnto mas alto
    print("--------------------------------------------------------------")
    print(">> RESULTADO <<")
    print ("La imagen pertenece a la clase--->",f[0])#imprime el elemento mas alto
    

#Parametros: nombre de la imagen
#Descripcion: Extrae las 14 caracteristicas de la nueva instancia(imagen)
#Variables de retorno: linea de tipo string que contiene todos los datos de la nueva instancia, 
#   concatenados y separados por comas
def instanciaN(nombre):
    img=mpimg.imread(nombre)
    #print ("\n>>EXTRAYENDO DATOS DE LA NUEVA INSTANCIA <<")
    vp1=p1(img)#Propiedad 1: #columnas/#filas 
    vp2=p2(img) #Propiedad 2:  #1's/ tamaño total de la imagen  
    vp3=p3(img) #Propiedad 3:#1's/columnas en la #fila/2
    vp4=p4(img) #Propiedad 4:#1's/columnas en la #fila/4
    vp5=p5(img) #Propiedad 5:#1's/columnas en la 3(#fila/4)
    vp6=p6(img) #Propiedad 6:#1's/filas en la #columnas/2
    vp7=p7(img) #Propiedad 7:#1's/filas en la #columnas/4
    vp8=p8(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp9=p9(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp10=p10(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp11=p11(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp12=p12(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp13=p13(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    vp14=p14(img) #Propiedad 8:#1's/filas en la 3(#columnas/4)
    #se concatenan todos los valores de cada imagen separados por una coma
    linea=str(vp1)+","+str(vp2)+","+str(vp3)+","+str(vp4)+","+str(vp5)+","+str(vp6)+","+str(vp7)+","+str(vp8)+","+str(vp9)+","+str(vp10)+","+str(vp11)+","+str(vp12)+","+str(vp13)+","+str(vp14)

    return linea


#Parametros: Ninguno
#Descripcion:es el menu principal donde se man
def menu():
    abrirImagen()#mandamos a llamar a la funcion abrir imagen
    
    print("\n\nInserta la direccion de la imagen: ejemplo 0-9/8/8_200.png ")
    #leer nombre de la imagen
    nombre=input()
    dis=leerCSV(nombre)#representa el arreglo con los vecinos mas cercanos
    print("Inserta el valor de K")
    #leer el valor de k-vecinos
    k=int(input())#convertidor de string a numero
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print("******* INFORMACIÓN GENERAL *******")
    print("Nùmero de Instancias en el Dataset: 2376")
    print("Nùmero de Características por cada instancia: 14")
    print("Nùmero de Clases: 10")
    for i in range(0,10):#impresion de clases 0 a 9
        print("Clase:",i)
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    vecinos=menorMayor(dis,k)# representa el arreglo de vecinos ordenados de menor a mayor
    print("Valor K=",k)
    j=0
    for i in vecinos:#recorre el arreglo de vecinos ordenados
        j+=1
        ##print("#",j,i)
        print("No.",j,"#Instancia",i[0],"Clase:",i[1],"Distancia:",i[2])
    kv=kvecinos(vecinos)#retorna el arreglo con las repeticiones
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print(">> RESUMEN <<")
    for h in kv:#recorre el arreglo con las repeticiones
        print ("Clase",h[0],"=",h[1])#impresion de cada elemento del arreglo
    listaOrd(kv)#funcion que muestra el resultado final
    
    
    

menu()#manda a traer a la funcion menu
Status 
