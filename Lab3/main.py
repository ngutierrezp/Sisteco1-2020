

##################################
# Lab 3: Cryptography
##################################



import numpy as np
from sympy import Matrix

ALPHABET = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",",","."," ","-","?"]



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

    









    '''

    cipher_matrix = []
    colnum = np.shape(matrix_key)[1]
    cipher_message = ""

    for letter in message:        
        index = ALPHABET.index(letter)
        cipher_matrix.append( index )
        range()

    mod = len(cipher_matrix) % colnum

    
    if mod != 0 :
        for i in range(colnum - mod):
            index = ALPHABET.index('-')
            cipher_matrix.append( index )
    
    np_array = np.array(cipher_matrix)
    
    np_array = np.reshape(np_array,(colnum,-1),order='F')
    
    result_matriz = np.matmul(matrix_key, np_array) % len(ALPHABET)

    for row in np.transpose(result_matriz):
        for index in row:
            
            cipher_message += ALPHABET[int(index)]


    return(cipher_message)

    
def getFactorMod(number,mod_number):
    
    for i in range(mod_number):
        
        if i* int(number) % mod_number == 1:
            return i



def hill_decrypted(matrix_key,message):

    inverse_matrix = Matrix(matrix_key)
    inverse_matrix = inverse_matrix.inv_mod(len(ALPHABET)) # modular inverse matrix
    inverse_matrix = np.array(inverse_matrix)
    print(inverse_matrix)

    new_matrix_key = []
    for row in inverse_matrix:
        for i in row:
            new_matrix_key.append(int(i))
    
    new_matrix_key = np.array(new_matrix_key).reshape(np.shape(matrix_key)[0],np.shape(matrix_key)[1])


    decrypted_matrix = []
    colnum = np.shape(new_matrix_key)[1]
    decrypted_message = ""

    for letter in message:        
        index = ALPHABET.index(letter)
        decrypted_matrix.append( index )
    
    np_array = np.array(decrypted_matrix)
    

    np_array = np.reshape(np_array,(colnum,-1),order='F')
    
    
    result_matriz = np.matmul(new_matrix_key, np_array) % len(ALPHABET)
    
    
    
    for row in np.transpose(result_matriz):
        for index in row:
            decrypted_message += ALPHABET[int(index)]
    

    return(decrypted_message)







a_2d = np.array([6,24,1,13,16,10,20,17,15]).reshape((3, 3))
print(a_2d)

mes = hill_cipher(a_2d,"mi nombre es nicolas y el---- tuyo cual es ")
print(mes)
mes2 = hill_decrypted(a_2d,mes)
print(mes2)



