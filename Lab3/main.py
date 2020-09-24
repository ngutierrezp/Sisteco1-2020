##################################
# Lab 3: Cryptography
##################################

# Nicolás Gutiérrez
# nicolas.gutierrez.p@usach.cl


import numpy as np
from os import system
import sys
import time 
import random
import math

### importamos los modulos:

from modules.menu import main_menu
from modules.cipher import hill_cipher, hill_decrypted
from modules.alphabet import getAlphabet
from modules.utilities import getRandomKey, getModularMatrix


# NOTA: Ejecutar desde main.py



if __name__ == "__main__":
    op = 0
    key = []

    message = ""

    while not (op in [6,9]):
        op = main_menu(key)

        if op == 1: 
            key = []
        elif op == 2:
            message = input('Ingrese el mensaje a cifrar : ')
            print("Tamaño de mensaje : "+ str(sys.getsizeof(message))+ " Bytes")
            print("Cifrando mensaje ...")
            start = time.time()
            mes_cipher = hill_cipher(key,message)
            end = time.time()
            print("El cifrado ha tardado : " + str(end-start) + " segundos")
            print('Mensaje cifrado: \n')
            print(mes_cipher)
            print('\n')
            input("Precione cualquier tecla para continuar ... ")
        elif op == 3:
            fileName = input('Ingrese el nombre / dirección del archivo a leer: ')
            try:
                print('Cifrando Archivo ...')
                f1 = open('./cipher.txt','w',encoding='utf-8')
                f = open(fileName,'r',encoding='utf-8')
                list_lines = f.read().splitlines()
                for line in list_lines:
                    cipher_line = hill_cipher(key,line)
                    f1.write(cipher_line)
                    f1.write('\n')
                f.close()
                f1.close()
                print('Archivo cifrado en cipher.txt')
                input("Precione cualquier tecla para continuar ... ")

            except:
                print('[ERROR]: No fue posible abrir el archivo, verifique el nombre o ubicación!')
        elif op == 4: 
            message = input('Ingrese el mensaje a descifrar : ')
            print("Descifrando mensaje ...")
            
            mes_decipher = hill_decrypted(key,message)
            
            print('Mensaje Descifrado: \n')
            print(mes_decipher)

            print("\n")
            input("Precione cualquier tecla para continuar ... ")
        elif op == 5: 
            fileName = input('Ingrese el nombre / dirección del archivo a leer: ')
            try:
                print('Descifrando Archivo ...')
                f1 = open('./descipher.txt','w',encoding='utf-8')
                f = open(fileName,'r',encoding='utf-8')
                list_lines = f.read().splitlines()
                for line in list_lines:
                    descipher_line = hill_decrypted(key,line)
                    f1.write(descipher_line)
                    f1.write('\n')
                f.close()
                f1.close()
                print('Archivo descifrado en descipher.txt')
                input("Precione cualquier tecla para continuar ... ")
            except:
                print('[ERROR]: No fue posible abrir el archivo, verifique el nombre o ubicación!')
            
        elif op == 7: 
            key = getRandomKey(len(getAlphabet()))
        elif op == 8: 
            key = []
            det = 0

            while det == 0:
                print('''
                    La Clave a ingresar debe cumplir ciertas condiciones:
                        1.- El total de numeros debe ser un numero cuadratico. Ejemplo:
                                2 , 4 , 9 , 16 , 25 .... etc
                        2.- Solo se deben ingresar numeros
                        3.- El determinante de la clave a ingresar debe ser distinto de 0
                        4.- Los numeros deben estar separados por UN espacio
                    ''')
                string_key = input("Ingrese la serie de numeros: ")
                try:
                    list_key = string_key.split()
                    for char in list_key:
                        key.append(int(char))
                    size = int( math.sqrt(len(key)) )
                    key = np.array(key)
                    key = np.reshape(key, (size,size))
                    getModularMatrix(key)
                    det = 1
                except:
                    print('[ERROR]: La matriz ingresada no cumple con las condiciones!!')
                    det = 0
                    key = []
                    
    print('Adiós')
            




