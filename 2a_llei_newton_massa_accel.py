def segona_llei_newton(massa, acceleracio):
    # Calcula la força utilitzant la fórmula F = ma
    forca = massa * acceleracio
    return forca

# Exemple d'ús de la funció
massa = 5  # en kg
acceleracio = 10  # en m/s^2
forca_resultant = segona_llei_newton(massa, acceleracio)
print("La força resultant és:", forca_resultant, "N")
