
import numpy as np
from sympy import Matrix
import random
from modules.alphabet import getAlphabet

def getModularMatrix(matrix):

    '''
    ------------
    DESCRIPCIÓN:
    Función que se encarga de encontrar la matriz modular inversa.

    :param matrix:  (numpy matrix) 
        Representa la llave que se utiliza para el cifrado. Debe ser
        una matriz cuadrada cuyo determinante sea distinto de 0 ya que debe
        ser posible invertirla.


    :return:        (numpy matrix)       
        La función da como salida una matriz que representa la matriz modular
        inversa.
    '''

    ALPHABET = getAlphabet()
    inverse_matrix = Matrix(matrix)
    # matriz modular inversa
    inverse_matrix = inverse_matrix.inv_mod(len(ALPHABET)) 
    inverse_matrix = np.array(inverse_matrix)
    
    # cambio de tipo de datos.
    new_matrix = []
    for row in inverse_matrix:
        for i in row:
            new_matrix.append(int(i))
    
    new_matrix = np.array(new_matrix).reshape(np.shape(matrix)[0],np.shape(matrix)[1])

    return (new_matrix)



def getRandomKey(mod):
    '''
    ------------
    DESCRIPCIÓN:
    Función que de generar una key valida para hacer el cifrado.

    :param mod:  (int) 
        Como es necesario que la matriz a generar tenga una inversa modular
        es necesario saber por que modulo se debe realizar.


    :return:        (numpy matrix)       
        La función da como salida una matriz que representa la llave (key).
    '''
    sizekey = [2,3,4,5,6]

    size = sizekey[random.randint(0, len(sizekey)-1)]

    det = 0
    key = []
    while det == 0:
        key = []
        for _ in range(size*size):
            key.append(random.randint(0,29))
        key = np.array(key)

        key = np.reshape(key,(size,size))

        try:
            inverse_matrix = Matrix(key)
            inverse_matrix = inverse_matrix.inv_mod(mod) 
            det = 1
        except:
            det = 0

    return(key)

