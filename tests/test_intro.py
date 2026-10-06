from main import addition, soustraction


def test_addition():
    resultat = addition(2, 3)

    assert resultat == 7


def test_soustraction():
    resultat = soustraction(3, 2)

    assert resultat == 1
