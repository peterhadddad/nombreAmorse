import math
def repeter(chiffre, string):
    repetition = ""
    for i in range(chiffre):
        repetition += string
    return repetition


def chiffre(number):
    nombreMaximale = 5
    if number >= 0 and number <= 5:
        return repeter(nombreMaximale - (nombreMaximale - number), ".") + repeter(nombreMaximale - number, "-")
    if number >= 6 and number <= 9:
        return repeter(number - nombreMaximale, "-") + repeter(abs(number - nombreMaximale - nombreMaximale), ".")


def extraireChiffre(nombre, rang):
    return (nombre // rang) % 10


def trouveRang(numero, nombre):
    return (numero // nombre)


def morse(entier):
    if entier >= 0 and entier <= 9:  # un seul chiffre a convertir
        return chiffre(entier)
    nbChiffres = int((math.log10(entier))) + 1  # extraire le nombre de

    resultat = ''
    for i in range(1, nbChiffres + 1):

          resultat += chiffre((entier // 10 ** (nbChiffres - i)) % 10)
          if i < nbChiffres:
               resultat += ' '  # eviter un espace en trop
    return resultat


print(morse(360))