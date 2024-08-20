from datetime import date

print("La fehca de hoy es: " + str(date.today()))

parsecs = int(input("Ingresa el número de parsecs: "))
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")