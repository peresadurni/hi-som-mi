def primera_llei_newton(forces):
    suma_forces = sum(forces)  # Suma de totes les forces
    if suma_forces == 0:
        return "L'objecte romandrà en repòs o en moviment rectilini uniforme."
    else:
        return "L'objecte experimentarà un canvi de moviment a causa de les forces externes."

# Exemple d'ús de la funció
forces = [0, 0, 0]  # Exemple de forces que actuen sobre l'objecte (en aquest cas, cap força)
resultat = primera_llei_newton(forces)
print(resultat)