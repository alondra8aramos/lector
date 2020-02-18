#!/usr/bin/python3
import lector
import argparse

def suma_diccionario(dp):
  suma = 0
  for k,v in dp.items():
    suma += v
  return suma
  
  
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

def imprime_diccionario( dp):
    listita=[]
    lista = [ (k,v) for k,v in dp.items() ]
    lista_ordenada = sorted(lista, key = lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
      listita.append(1)
    return listita

def total_diccionario( total):
    total=[]
    lista = [ (k,v) for k,v in total.items() ]
    lista_ordenada = sorted(lista, key = lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
      total.append(tupla[1])
    return listita

def porcentaje(num_total, num_palabras):
   x = (num_palabras * 100) / num_total
   return x
    
def main ( archivo, archivo_stopwords ):
  texto = lector.leer_archivo(archivo)
  lista_palabras = texto.split(" ")
  total = len(lista_palabras)
  print('TOTALES', total)
  stopwords = lector.leer_stopwords(archivo_stopwords)

  dpc = dict()
  dps = dict()
  for palabra in lista_palabras:
    p = palabra.lower()
    if p in stopwords: #es stopword?
      if p in dps: #Ya existe?
        dps[p] += 1 #agregamos 1
      else:
        dps[p] = 1 #inicial con 1
    else:
      if p in dpc:
        dpc[p] += 1
      else:
        dpc[p] = 1
  suma_palabras_clave = suma_diccionario(dpc)
  suma_palabras_stop = suma_diccionario(dps)
  listadpc = imprime_diccionario(dpc)
  listadps = imprime_diccionario(dps)
  print ("Las claves son", suma_palabras_clave)
  print("Las stopwords son", suma_palabras_stop)
  unicadpc = sumalista(listadpc)
  unicadps = sumalista(listadps)
  print("Claves unicas", unicadpc)
  print("Stop unicas", unicadps)
  porDPC= porcentaje((total), unicadpc)
  porDPS = porcentaje((total), unicadps)
  print('% claves unicas', porDPC)
  print('% sw unicas', porDPS)
  
  
  
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help=
"nombre de archivo", required=True)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help=
"nombre de stopword", required=False, default="spanish_stopwords.txt")
    args = parser.parse_args()
    archivo = args.archivo
    archivo_stopwords= args.stopwords
    main(archivo, archivo_stopwords)