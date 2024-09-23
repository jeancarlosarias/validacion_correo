import re

correo = input("Ingrese los correos electronicos(separados por ','): ").split(",")


def Validacion(correo):
    ###Comprobando la validacion en individual###
    
    # validacion = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo)
    # if validacion:
    #     print("coinciden")
    # else:
    #     print("No")   
    
    ###La validacion ya hecha por listas###
    total = len(correo)
    Buenas = 0
    Malas = 0
    conteo = 0
    for x in correo: ###Bucle para comprobar la coincidencia de los correos, con su respectivo conteo###
        if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", x): 
            conteo += 1
            Buenas += 1
            print(f"El correo numero {conteo} coincide")
        else:
            conteo += 1
            Malas += 1
            print(f"El correo numero {conteo} no coincide")
            
    print(f"De los {total} correos, hay un total de: Buenas = {Buenas} y Malas = {Malas}")
        
Validacion(correo)

# Jean Carlos Arias, estuvo aqui, 
# Jean Carlos Santana
# Rama de jose rafael.
# Yendy tambien estuvo aqui
# i peed on your wife
