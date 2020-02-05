#! /urs/bin/python3

#importacion de librerias

#2 funciones
def leer_archivo(rute):    # leer archivo
   fh = open(rute, 'r')
   text = fh.read()
   fh.close()   
                                 #limpia texto
   text.strip('\n')
   lines = text.splitlines()
   clean_text = " ".join(lines)
   return clean_text

def contar_palabras(clntext):
   DC = dict()
   txt = clntext.split(" ")
   for x in txt:
     word = x.strip(',.')
     if word in DC:
        DC[word] += 1 
     else:
        DC[word] = 1
   return DC


def main( archivo ):
    ''' main() recibe nombre de archivo lo abre 
    y cuenta palabras repetidas '''
    texto = leer_archivo( archivo )
    dip = contar_palabras( texto )
    print( dip )

#3 ejecucion de main 
if __name__ == "__main__":
    archivo  = "/tmp/episodio4.txt"
    main(archivo)

