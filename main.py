""" 
El programa es un sistema de gestión de datos de mascotas que permite al usuario realizar las siguientes operaciones:

-Ingresar datos de una mascota (nombre, número de chip y tipo (gato, perro)) y los almacena en listas separadas.
-Buscar una mascota por su número de chip y mostrar su tipo y nombre si se encuentra en las listas.
-Mostrar listas separadas con los nombres de los gatos y perros registrados.
-Modificar el nombre de una mascota utilizando su número de chip si se encuentra en las listas, mostrando un mensaje de confirmación o si el chip no se encuentra."""

import funciones as fn


nombre_mascota_gato=[]
nombre_mascota_perro=[]

numero_chip_gato=[]
numero_chip_perro=[]

flag= True
while flag == True:
   
    print("\n======Menú=====")
    print("1: Ingresar datos de la mascota")
    print("2: Buscar mascota según su chip ")
    print("3: Mostrar nombre de los gatos registrados  ")
    print("4: Mostrar nombre de los perros registrados  ")
    print("5: Modificar nombre de las mascotas ")
    print("6: Salir \n" )   
   
    try:
        option = int(input("Ingrese su opción: "))
        
        if option == 1:
            
            flag_nombre = False
            while flag_nombre == False:
                nombre= input("\nIngresar el nombre de la mascota : ")   
                flag_nombre = fn.validar_nombre(nombre)
                if flag_nombre == False:
                    print("Ingrese un nombre válido") 


            flag_chip = False
            while flag_chip == False:
                chip= int(input("Ingresar el número del chip (8 digitos) : "))
                flag_chip = fn.validar_chip(chip, numero_chip_gato, numero_chip_perro)
                if flag_chip == False:
                    print("Ingrese un chip válido")   


            flag_tipo = False
            while flag_tipo == False:
                tipo= input("Ingresar el tipo de mascota (Perro/Gato) : ")
                flag_tipo = fn.validar_tipo(tipo)
                if flag_tipo == False:
                    print("Ingrese un tipo correcto")
                  
               
            fn.segun_tipo(nombre,nombre_mascota_gato, nombre_mascota_perro, chip,numero_chip_gato, numero_chip_perro, tipo)
            print(f"Ingresado al sistema correctamente : {nombre} / {chip} / {tipo} ")
            print()


        elif option == 2:
        
            chipp= int(input("\nIngresar el número del chip : "))
            bool, tipo, nombre = fn.busqueda_chip(chipp, numero_chip_gato, numero_chip_perro,nombre_mascota_gato, nombre_mascota_perro )
            if bool ==  True:
                print(f"Tipo: {tipo}")
                print(f"Nombre: {nombre}")
                
                        
            if bool ==  False:
                print("El chip no está registrado")
            
            
        elif option ==3:
            print("\nListado de gatos registrados:")
            print(nombre_mascota_gato)
            
        elif option ==4:
            print("\nListado de perros registrados:")
            print(nombre_mascota_perro)
       
        elif option ==5:
            chip= int(input("\nIngrese el número del chip :"))
            nombre= input("Ingrese el nuevo nombre: ")
            estado = fn.cambiar_nombre(chip, nombre, numero_chip_gato, numero_chip_perro,nombre_mascota_gato, nombre_mascota_perro )
            print(estado)


        elif option == 6:
            print("Salir del programa...")
            flag= False

    except:
        print("\nIngrese una opción válida\n")

