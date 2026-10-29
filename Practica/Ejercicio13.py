palabra = input("escribe una palabra:")
Vocales = 0

for letra in palabra.lower():
    if letra in "aeiou":
        Vocales += 1

print("Tiene", Vocales, "vocales")