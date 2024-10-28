#En aquest exemple, la funció capacitat_canal pren l'amplada de banda del canal (en Hz) i el 
#nivell de soroll (en dB) com a paràmetres. Utilitza la fórmula de Shannon per calcular 
#la capacitat del canal i retorna el resultat en bits per segon. Finalment, es mostra la 
#capacitat calculada del canal. Pots ajustar els valors de l'amplada de banda i el nivell de 
#soroll segons el teu cas d'ús específic.

import math

def capacitat_canal(bandwidth, noise):
    # Càlcul de la capacitat del canal utilitzant la fórmula de Shannon
    capacity = bandwidth * math.log2(1 + (bandwidth / noise))
    return capacity

# Exemple d'ús de la funció
bandwidth = 1000000  # Amplada de banda del canal en Hz
noise = 10  # Nivell de soroll en dB
capacitat = capacitat_canal(bandwidth, noise)
print("La capacitat del canal és:", capacitat, "bits per segon")