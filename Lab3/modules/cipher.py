
import numpy as np
from modules.alphabet import getAlphabet, addCharAlphabet
from sympy import Matrix


def hill_cipher(matrix_key,message):
    '''
    ------------
    DESCRIPCIÓN:
    Función para el cifrado de hill, su funcionamiento es por medio de la multiplicación
    de matrices, por lo que es necesario primeramente el uso de la libreria Numpy.

    :param matrix_key:  (numpy matrix) 
        Representa la llave que se utiliza para el cifrado. Debe ser
        una matriz cuadrada cuyo determinante sea distinto de 0 ya que debe
        ser posible invertirla.

    :param message:     (string)
        Representa el mensaje que se va a cifrar, debe contener solo letras  
        letras minusculas y puede contener caracteres especiales.


    :return:            (string)       
        La función da como salida el mensaje cifrado, este mensaje puede que sea
        más largo que el primero debido a que se añadan caracteres especiales 
        para completar la matriz.
    ------------
    FUNCIONAMIENTO:
    
    El funcionamiento de la función se limita a la multiplicación de matrices, si se
    tiene la matriz llave K, y el mesnsaje a cifras, primero se transforma el mensaje
    a Matriz con los indices del alfabeto definido. Por ejemplo si queremos cifrar
    'hola', los indices  serian : 7, 15, 11, 0 :

        hola ->      7   11
                    15    0

    Por lo que ahora basta con multiplicar la matriz K por la matriz del mensaje X
    quedando una transformación lineal de la forma Y= K*X

    Para obtener el mesaje cifrado solo basta con recorrer la matriz transpuesta Y
    y agregar cada letra a un buffer string para devolverlo como respuesta.

    ------------
    NOTAS ADICIONALES

    En el caso de que la matriz llave K sea más grande que la matriz X, a esta ultima
    se le agrega tantos caracteres especiales '■' como espacios que falten en la matriz.


    En el caso de que no exista un caracter en el alfabeto, este se agrega y se vuelve a
    hacer el proceso de cifrado.

    '''
    ALPHABET = getAlphabet()
    matrix_message = []
    colnum = np.shape(matrix_key)[1] # numero de columnas de la matriz llave
    cipher_message = ""

    for letter in message:
        if letter in ALPHABET:        
            index = ALPHABET.index(letter)
            matrix_message.append( index )
        else:
            addCharAlphabet(letter)
            return hill_cipher(matrix_key,message)
        
    # Calculo para añadir caracteres especiales
    mod = len(matrix_message) % colnum

    if mod != 0 :
        for _ in range(colnum - mod):
            index = ALPHABET.index('■')
            matrix_message.append( index )
    
    matrix_message = np.array(matrix_message)
    
    # Se transforma un arreglo a matriz
    matrix_message = np.reshape(matrix_message,(colnum,-1),order='F')
    
    # multiplicacion de matices
    result_matriz = np.matmul(matrix_key, matrix_message) % len(ALPHABET)

    # iteración de matriz transpuesta.
    for row in np.transpose(result_matriz):
        for index in row:
            
            cipher_message += ALPHABET[int(index)]

    return(cipher_message)

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




        
        


def hill_decrypted(matrix_key,message):
    
    '''
    ------------
    DESCRIPCIÓN:
    Función para decifrado de una mensaje por hill. El proceso es bastante similar que en el cifrado
    que que tambien es necesario hacer una multiplicación de matrices. De echo el proceso matematico 
    es simular a despejar una incognita. Recordemos que Y = K*X -> X = K^-1*Y.

    :param matrix_key:  (numpy matrix) 
        Representa la llave que se utiliza para el cifrado. Debe ser
        una matriz cuadrada cuyo determinante sea distinto de 0 ya que debe
        ser posible invertirla.

    :param message:     (string)
        Representa el mensaje que se va a descifrar, debe contener solo letras  
        letras minusculas y puede contener caracteres especiales.


    :return:            (string)       
        La función da como salida el mensaje descifrado.
        
    ------------
    FUNCIONAMIENTO:
    
    El funcinamiento realmente es el mismo para el cifrado ya que se multiplican
    matrices, la diferencia que radica es en que se debe encontrar la matriz
    modular inversa de K. 

    La matriz modular inversa es aquella que al invertir la matriz aplicando el
    modulo del largo del alfabeto, se obtenen los numeros inversos para los 
    indices de ese mismo alfabeto. En resumen es el complemento inverso de la matriz
    K.

    '''
    ALPHABET = getAlphabet()
    # matriz modular inversa
    inverse_matrix = getModularMatrix(matrix_key)

    decrypted_matrix = []
    colnum = np.shape(inverse_matrix)[1]
    decrypted_message = ""

    # se encuentra el indice para la matriz 
    for letter in message:        
        index = ALPHABET.index(letter)
        decrypted_matrix.append( index )
    
    np_array = np.array(decrypted_matrix)
    

    np_array = np.reshape(np_array,(colnum,-1),order='F')
    
    
    result_matriz = np.matmul(inverse_matrix, np_array) % len(ALPHABET)
    
    
    # se desencripta cada caracter reemplazando los agregados por espacios vacios.
    for row in np.transpose(result_matriz):
        for index in row:
            if ALPHABET[int(index)] == '■':
                decrypted_message += ""
            else:
                decrypted_message += ALPHABET[int(index)]
    

    return(decrypted_message)
