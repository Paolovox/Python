
#qui sono definite le funzioni
#def==funzione
#stampa==nome della funzione
#(stringa)==argomento che prende in pasto la funzione
#return==ritorna un valore o nulla in questo caso la stringa passata come argomento

def stampa(stringa):
    return stringa


#ritorna la lunghezza di una stringa

def cont(stringa):
    c=0
    for lettera in stringa:
        c=c+1

    return c


#ritorna la somma dei numeri della lista
def somma(lista):
    somma = 0
    for numero in lista:
        somma = somma + numero
    return somma


#ritorna il numero di "-" presenti nella stringa, altrimenti -1
def contaTrattini(stringa):
    c=0
    #for ogni lettera nella stringa controlla se è un trattino, se lo è incrementi c

    return c


#ritorna True se nella stringa ci sono solo lettere, False altrimenti
def controllaStringa(stringa):
    
    return True


#stampa un quadrato di dimensione n*n, se n è negativo stampa "N non è valido cazzo di Buddha"
#Es n=2 stamperà  * *
#                 * *

def stampaQuadrato(n):
    stringa = str()

    return stringa


#stampa un triangolo se n è dispari, isoscele con base pari a n         se n è pari stampa "Porco Dio bestia"
#Es n = 3 stamperà    *
#                    * *
#                   * * *
def stampaTriangolo(n):
    stringa = str()

    return stringa


if __name__ == "__main__":

    print("la lunghezza della stringa è: ")
    print(cont("niculicchio"))

    lista = [1,4,23]
    print("La somma della lista è :"+str(somma(lista)))    #str(valore) converte un intero, float o double in una stringa

    #stampa il tuo nome
    #stampa("mionome")

    #stampa le lettere del tuo nome divise da trattini "p-a-o-l-o"
    #for lettera in stampa("mionome")


    print(contaTrattini("ciao"))       #deve ritornare 0
    print(contaTrattini("b-a-f-a-n-g-u-l-o"))    # deve ritornare 8
    print(contaTrattini("----FUCKKK OIECCW ewiwe--ascvsavvs-avfv-rev-erv-rverv-)()(E)("))  #deve tornà 11

    print(controllaStringa("15-06-2001")) #false
    print(controllaStringa("ZiPippo1"))   #false
    print(controllaStringa("Bafang"))     #true

    print(stampaQuadrato(4))
    print(stampaQuadrato(-4265428))
    print(stampaQuadrato("ciao"))

    print(stampaTriangolo(3))
    print(stampaTriangolo(4))
    print(stampaTriangolo(-1))






