from bagels.bagels import Bagels


def test_getSecretNum():
    test_game1 = Bagels(num_digits=3)
    assert len(test_game1.getSecretNum()) == 3

    test_game2 = Bagels(num_digits=5)
    assert len(test_game2.getSecretNum()) == 5


def test_getClues():
    test_game = Bagels(num_digits=3)
    assert test_game.getClues('123', '123') == 'You got it!'
    assert test_game.getClues('123', '456') == 'Bagels'
    assert test_game.getClues('123', '132') == 'Fermi Pico Pico'
