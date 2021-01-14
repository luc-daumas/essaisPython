def estBisextile(annee):
    """Retourne true si l'annee est bisextile, false sinon
    un annee est bisextile si elle est divisible par 4 et non divisible par 100, ou si elle est divisible par 400
    >>> estBisextile(2021)
    False
    >>> estBisextile(1900)
    False
    >>> estBisextile(2020)
    True
    >>> estBisextile(2000)
    True
    """
    if annee % 400 == 0:
        return True
    if annee % 100 == 0:
        return False
    if annee % 4 == 0:
        return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    while (True):
        annee = input("Entrez une année : ")
        if not annee:
            print("Fin")
            exit()
        annee = int(annee)
        if estBisextile(annee):
            print("L'année {annee} est bisextile")
        else:
            print("l'année' {annee} n'est pas bisextile")
