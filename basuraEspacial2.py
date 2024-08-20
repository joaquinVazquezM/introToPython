object_size = int(input("Indica el tamaño del objeto: "))
distancia = int(input("Indica la distancia de la basura espacial en km: "))

if object_size > 10 and distancia <= 1000:
    print("¡ALERTA! Necesitamos realizar maniobras evasivas")
else:
    print("El objeto no representa ninguna amenaza")