def afficheNom(name):
    """Affiche le nom
    >>> afficheNom("exemple nom")
    ==> exemple nom
    """
    nomAAfficher = "==> " + name
    print(nomAAfficher)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()
    afficheNom('PyCharm')
