import find_pal as fp

palabras_frases = fp.FindPal.encuentra_palabras()
pal_fr = fp.FindPal("palabras.txt", "frases.txt")
print("Palabras: ", pal_fr.palabras)
print("Frases: ", pal_fr.frases)
pal_frases = palabras_frases.encuentra_palabras()
print("Contador de palabras en frases: \n", pal_frases)
