
def validar_nombre(nombre):
    if len(nombre) >= 3:
        return True
    else:
        return False
    

# La función verifica si el número de chip es único y si está dentro del rango de 10000000 a 99999999
def validar_chip(chip, numero_chip_gato, numero_chip_perro):  
    
    for i in numero_chip_gato:
        if i == chip:
            return False
    for i in numero_chip_perro:
        if i == chip:
            return False

    if chip >= 10000000 and chip <= 99999999:
        return True
    else:
        return False
    
# Verifica si el tipo está escrito correctamente, sin importar si está en mayúsculas o minúsculas. 
def validar_tipo(tipo):

    if tipo.upper() == "PERRO":       
        return True
    elif tipo.upper() == "GATO":         
         return True
    else:        
        return False


#Se encarga de agregar el nombre y el número de chip de la mascota a la lista adecuada según el tipo de mascota (Perro o Gato).
def segun_tipo(nombre,nombre_mascota_gato, nombre_mascota_perro, chip,numero_chip_gato, numero_chip_perro, tipo):

    if tipo.upper() == "PERRO":
        nombre_mascota_perro.append(nombre)
        numero_chip_perro.append(chip)        
           
    elif tipo.upper() == "GATO":
        nombre_mascota_gato.append(nombre)
        numero_chip_gato.append(chip)
        
    
#Busca el número de chip en las listas de números de chip. Si lo encuentra, determina si la mascota es un gato o un perro y devuelve True junto con el tipo y el nombre de la mascota. Si el número de chip no se encuentra, devuelve False junto con el tipo y el nombre vacíos.
def busqueda_chip(chipp, numero_chip_gato, numero_chip_perro,nombre_mascota_gato, nombre_mascota_perro ):

    for i in numero_chip_gato:
        if chipp == i:
            tipo = "Gato"
            posicion= numero_chip_gato.index(chipp)
            nombre = nombre_mascota_gato[posicion] 
            return True, tipo, nombre

    for i in numero_chip_perro:
        if chipp == i:
            tipo = "Perro"
            posicion= numero_chip_perro.index(chipp)
            nombre = nombre_mascota_perro[posicion]                   
            return True, tipo, nombre

    tipo=""
    nombre=""
    return False, tipo


#Cambia el nombre de la mascota con el número de chip solicitado, solo si el chip se encuentra en una de las listas. Devuelve un mensaje indicando el resultado del cambio de nombre o si el número de chip no se encontró.
def cambiar_nombre(chip, nombre, numero_chip_gato, numero_chip_perro,nombre_mascota_gato, nombre_mascota_perro ):

    for i in numero_chip_gato:
        if chip == i:
            posicion= numero_chip_gato.index(chip)
            nombre_original = nombre_mascota_gato[posicion]
            nombre_mascota_gato[posicion] = nombre
            estado= f"Nombre {nombre_original} cambiado a {nombre}"
            return estado
    
    for i in numero_chip_perro:        
        if chip == i:
            posicion= numero_chip_perro.index(chip)           
            nombre_original = nombre_mascota_perro[posicion]
            nombre_mascota_perro[posicion] = nombre
            estado= f"Nombre {nombre_original} cambiado a {nombre}"
            return estado

    estado = f"No se encontró el chip {chip}"
    return estado



