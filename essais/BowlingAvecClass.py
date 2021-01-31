#!/usr/bin/python3

class Tour :

    def __init__(self, quillesAuPremierLancer = 0, quillesAuDeuxiemeLancer = 0, quillesAuTroisiemeLancer = 0):
        self.quillesAuPremierLancer = quillesAuPremierLancer
        self.quillesAuDeuxiemeLancer = quillesAuDeuxiemeLancer

    def estUnSpare(self):
        return self.quillesAuPremierLancer < 10 and self.quillesAuPremierLancer + self.quillesAuDeuxiemeLancer == 10

    def estUnStrike(self):
        return self.quillesAuPremierLancer == 10

    def calculLeScore(self, tourPlusUn, tourPlusDeux):
        """Retourne le nombre de points marqués pour un tour
        on fait la somme des 2 lancers
        si le tour est un spare, on ajoute le premier lancer du tour suivant
        si le tour est un strike, on ajoute les 2 lancers suivants
        >>> Tour(0, 0).calculLeScore(Tour(0, 0), Tour(0, 0))
        0
        >>> Tour(10, 0).calculLeScore(Tour(10, 0), Tour(10, 0))
        30
        >>> Tour(3, 7).calculLeScore(Tour(0, 0), Tour(0, 0))
        10
        >>> Tour(3, 7).calculLeScore(Tour(4, 6), DernierTour(5, 6, 7))
        14
        >>> Tour(5, 1).calculLeScore(Tour(0, 0), Tour(10, 0))
        6
        """
        score = self.quillesAuPremierLancer + self.quillesAuDeuxiemeLancer
        if self.estUnSpare() :
            score += tourPlusUn.quillesAuPremierLancer
        if self.estUnStrike() :
            score += tourPlusUn.quillesAuPremierLancer + tourPlusUn.quillesAuDeuxiemeLancer
            if tourPlusUn.estUnStrike() and tourPlusDeux:
                score += tourPlusDeux.quillesAuPremierLancer
        return score

    def calculAvantDernierScore(self, dernierTour):
        """Retourne le nombre de points marqués pour un tour
        on fait la somme des 2 lancers
        si le tour est un spare, on ajoute le premier lancer du tour suivant
        si le tour est un strike, on ajoute les 2 lancers suivants
        >>> Tour(0, 0).calculAvantDernierScore(DernierTour(0, 0, 0))
        0
        >>> Tour(10, 0).calculAvantDernierScore(DernierTour(10, 10, 10))
        30
        >>> Tour(3, 7).calculAvantDernierScore(DernierTour(10, 4, 3))
        20
        >>> Tour(3, 7).calculAvantDernierScore(DernierTour(0, 0, 0))
        10
        >>> Tour(5, 1).calculAvantDernierScore(DernierTour(10, 4, 3))
        6
        """
        score = self.quillesAuPremierLancer + self.quillesAuDeuxiemeLancer
        if self.estUnSpare() :
            score += dernierTour.quillesAuPremierLancer
        if self.estUnStrike() :
            score += dernierTour.quillesAuPremierLancer + dernierTour.quillesAuDeuxiemeLancer
        return score

class DernierTour :

    def __init__(self, quillesAuPremierLancer = 0, quillesAuDeuxiemeLancer = 0, quillesAuTroisiemeLancer = 0):
        self.quillesAuPremierLancer = quillesAuPremierLancer
        self.quillesAuDeuxiemeLancer = quillesAuDeuxiemeLancer
        self.quillesAuTroisiemeLancer = quillesAuTroisiemeLancer

    def calculLeScore(self):
        """Retourne le nombre de points marqués pour un tour
        on fait la somme des 3 lancers
        >>> DernierTour(0, 0, 0).calculLeScore()
        0
        >>> DernierTour(10, 10, 10).calculLeScore()
        30
        >>> DernierTour(3, 7, 0).calculLeScore()
        10
        >>> DernierTour(3, 7, 4).calculLeScore()
        14
        """
        score = self.quillesAuPremierLancer + self.quillesAuDeuxiemeLancer + self.quillesAuTroisiemeLancer
        return score

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    listeTours = [Tour(0, 0), Tour(10, 0), Tour(5, 5), Tour(2, 3), Tour(2, 3), Tour(2, 3), Tour(2, 3), Tour(2, 3), Tour(10, 0), DernierTour(2, 8, 4)]
    scoreTotal = 0
    score = 0
    for indiceTour in range(0, len(listeTours)):
         if indiceTour < 8:
             score = listeTours[indiceTour].calculLeScore(listeTours[indiceTour + 1], listeTours[indiceTour + 2])
         if indiceTour == 8:
             score = listeTours[indiceTour].calculAvantDernierScore(listeTours[indiceTour + 1])
         if indiceTour == 9:
             score = listeTours[indiceTour].calculLeScore()
         print("score tour {} = {}".format(indiceTour,score))
         scoreTotal += score

    print("score total = {}".format(scoreTotal))

    listeTours = [Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), Tour(10, 0), DernierTour(10, 10, 10)]
    scoreTotal = 0
    score = 0
    for indiceTour in range(0, len(listeTours)):
         if indiceTour < 8:
             score = listeTours[indiceTour].calculLeScore(listeTours[indiceTour + 1], listeTours[indiceTour + 2])
         if indiceTour == 8:
             score = listeTours[indiceTour].calculAvantDernierScore(listeTours[indiceTour + 1])
         if indiceTour == 9:
             score = listeTours[indiceTour].calculLeScore()
         print("score tour {} = {}".format(indiceTour,score))
         scoreTotal += score

    print("score total = {}".format(scoreTotal))