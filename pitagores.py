#Preguntant catets:
def pitagoras(catet1, catet2):
    hipotenusa = (catet1**2 + catet2**2)**0.5
    return hipotenusa

# Entrada dels catets per l'usuari
catet1 = float(input("Introdueix la longitud del primer catet: "))
catet2 = float(input("Introdueix la longitud del segon catet: "))

# Càlcul de la hipotenusa i impressió del resultat
hipotenusa = pitagoras(catet1, catet2)
print("La longitud de la hipotenusa és:", hipotenusa)