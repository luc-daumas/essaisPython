#!/usr/bin/python3

def estUnSpare(tour):
    return tour[0] < 10 and tour[0] + tour[1] == 10


def estUnStrike(tour):
    return tour[0] == 10


def calculLeScorePourUnTour(tour, tourPlusUn, tourPlusDeux = [0, 0]):
    """Retourne le nombre de points marqués pour un tour
    on fait la somme des 2 lancers
    si le tour est un spare, on ajoute le premier lancer du tour suivant
    si le tour est un strike, on ajoute les 2 lancers suivants
    >>> calculLeScorePourUnTour([0, 0], [0, 0], [0, 0])
    0
    >>> calculLeScorePourUnTour([1, 2], [1, 1], [1, 1])
    3
    >>> calculLeScorePourUnTour([10, 0], [10, 0], [10, 0])
    30
    >>> calculLeScorePourUnTour([3, 7], [0, 0], [0, 0])
    10
    >>> calculLeScorePourUnTour([3, 7], [4, 6], [5, 6, 7])
    14
    >>> calculLeScorePourUnTour([5, 1], [0, 0], [10, 0])
    6
    """
    score = tour[0] + tour[1]
    if estUnSpare(tour):
        score += tourPlusUn[0]
    if estUnStrike(tour):
        score += tourPlusUn[0] + tourPlusUn[1]
        if estUnStrike(tourPlusUn):
            score += tourPlusDeux[0]
    return score


def calculLeScorePourLeDernierTour(dernierTour):
    """Retourne le nombre de points marqués pour un tour
    on fait la somme des 3 lancers
    >>> calculLeScorePourLeDernierTour([0, 0, 0])
    0
    >>> calculLeScorePourLeDernierTour([10, 10, 10])
    30
    >>> calculLeScorePourLeDernierTour([3, 7, 0])
    10
    >>> calculLeScorePourLeDernierTour([3, 7, 4])
    14
    """
    score = dernierTour[0] + dernierTour[1] + dernierTour[2]
    return score


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    listeTours = [[0, 0], [10, 0], [5, 5], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [10, 0], [2, 8, 4]]
    scoreTotal = 0
    scoreTour = 0
    for indiceTour in range(0, len(listeTours)):
        if indiceTour < 8:
            scoreTour = calculLeScorePourUnTour(listeTours[indiceTour], listeTours[indiceTour + 1], listeTours[indiceTour + 2])
        if indiceTour == 8:
            scoreTour = calculLeScorePourUnTour(listeTours[indiceTour], listeTours[indiceTour + 1])
        if indiceTour == 9:
            scoreTour = calculLeScorePourLeDernierTour(listeTours[indiceTour])
        print("score tour {} = {}".format(indiceTour, scoreTour))
        scoreTotal += scoreTour

    print("score total = {}".format(scoreTotal))

    listeTours = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10, 10]]
    scoreTotal = 0
    scoreTour = 0
    for indiceTour in range(0, len(listeTours)):
        if indiceTour < 8:
            scoreTour = calculLeScorePourUnTour(listeTours[indiceTour], listeTours[indiceTour + 1], listeTours[indiceTour + 2])
        if indiceTour == 8:
            scoreTour = calculLeScorePourUnTour(listeTours[indiceTour], listeTours[indiceTour + 1])
        if indiceTour == 9:
            scoreTour = calculLeScorePourLeDernierTour(listeTours[indiceTour])
        print("score tour {} = {}".format(indiceTour, scoreTour))
        scoreTotal += scoreTour

    print("score total = {}".format(scoreTotal))
