def getAlphabet():
    '''
    ------------
    DESCRIPCIÓN:
    Función que obtiene el alfabeto desde un archivo de texto.

    :return:        (array)       
        Da como salida un arreglo con cada caracter del alfabeto
    '''
    f = open('./data/alphabet.txt','r',encoding='utf-8')

    line = f.readline()
    alphabet = []
    for letter in line:
        alphabet.append(letter)
    
    f.close()
    return(alphabet)

def addCharAlphabet(char):
    '''
    ------------
    DESCRIPCIÓN:
    Función que guarda en un archivo de texto (alfabeto)
    una caracter que no se encuentre.

    :param char:        (char)       
        Da como salida un arreglo con cada caracter del alfabeto
    '''
    f = open('./data/alphabet.txt','a')
    f.write(char)
    f.close()
