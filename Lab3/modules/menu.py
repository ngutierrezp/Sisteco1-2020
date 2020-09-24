
from os import system

def print_title(key):
    '''
    ------------
    DESCRIPCIÓN:
    Función encargada de desplegar el titulo del programa y dependiendo
    si existe una key, sera el modo de despliege

    :param key: (numpy array)

    '''

    try:
        system('clear')
    except:
        system('cls')
    
    print('''
                                                                                              ██████      
      ██████                                                                                ██      ██    
    ██      ██         _____ _  __               _         _    _ _____ _      _            ██      ██    
    ██      ██        / ____(_)/ _|             | |       | |  | |_   _| |    | |           ██            
  ██████████████     | |     _| |_ _ __ __ _  __| | ___   | |__| | | | | |    | |         ██████████████  
██              ██   | |    | |  _| '__/ _` |/ _` |/ _ \  |  __  | | | | |    | |       ██              ██
██      ██      ██   | |____| | | | | | (_| | (_| | (_) | | |  | |_| |_| |____| |____   ██      ██      ██
██      ██      ██    \_____|_|_| |_|  \__,_|\__,_|\___/  |_|  |_|_____|______|______|  ██      ██      ██
██              ██                                                                      ██              ██
  ██████████████                                                                          ██████████████  
        
    ''')


    if len(key) != 0:
        print('''
Llave cargada exitosamente!
      .--.
     /.-. '----------.
     \'-' .--"--""-"-'
      '--'
''')
        print(key)
        print("\n")

def main_menu(key):

    '''
    ------------
    DESCRIPCIÓN:
    Función encargada de desplegar las opciones del menu, dependiendo si existe una key
    se mostraran diferentes menus.

    :param key: (numpy array)


    :return: (int)
        se retorna un entero correspondiente a la opción escogida.

    '''

    print_title(key)
    if len(key) != 0:
        print("#------ Menu ------#")
        print('''
        1.- Borrar LLave
        2.- Cifrar Mensaje
        3.- Cifrar Archivo
        4.- Descifrar Mensaje
        5.- Descifrar Archivo
        6.- Salir
        ''')
        try:
            op = int(input('Ingrese un valor [1-6]: '))
        except:
            op = 0
        while not (op in [1,2,3,4,5,6]):
            print_title(key)
            print('[ERROR]: Debe ingresar un valor valido!')
            print("#------ Menu ------#")
            print('''
            1.- Borrar LLave
            2.- Cifrar Mensaje
            3.- Cifrar Archivo
            4.- Descifrar Mensaje
            5.- Descifrar Archivo
            6.- Salir
            ''')
            try:
                op = int(input('Ingrese un valor [1-6]: '))
            except:
                op = 0

    else:
        print("#------ Menu ------#")
        print('''
        1.- Generar Llave
        2.- Ingresar LLave
        3.- Salir
        ''')
        try:
            op = int(input('Ingrese un valor [1-3]: ')) + 6
        except:
            op = 0
        while not (op in [7,8,9]):
            print_title(key)
            print('[ERROR]: Debe ingresar un valor valido!')
            print("#------ Menu ------#")
            print('''
            1.- Generar Llave
            2.- Ingresar LLave
            3.- Salir
            ''')
            try:
                op = int(input('Ingrese un valor [1-3]: ')) + 6
            except:
                op = 0
    
    return (op)
    
