#!/usr/bin/python3

def marque(action, actionPrecedente):
    """Retourne le nombre de points marqués pour une action
    5 pour un essai, 2 pour un tir suivant un essai, 3 pour un autre tir
    >>> marque("essai", "tir")
    5
    >>> marque("essai", "essai")
    5
    >>> marque("tir", "tir")
    3
    >>> marque("tir", "essai")
    2
    """
    if action == "essai":
        return 5
    if action == "tir" and actionPrecedente == "essai":
        return 2
    if action == "tir" and actionPrecedente == "tir":
        return 3
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    listeAction = ["essai", "tir", "tir", "essai", "essai"]
    actionPrecedente = ""
    score = 0
    for action in listeAction:
        pointsMarques = marque(action, actionPrecedente)
        print("action {} => points marqués : {}".format(action, pointsMarques))
        score += pointsMarques
        actionPrecedente = action

    print("score final : {}".format(score))