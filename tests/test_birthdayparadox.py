from birthdayparadox.birthdayparadox import BirthdayParadox


def test_get_birthdays():
    test_game = BirthdayParadox()
    assert len(test_game.getBirthdays(10)) == 10


def test_get_match():
    test_game = BirthdayParadox()
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is None
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 1
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == 2
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 3]) == 3
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 4]) == 4
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 5]) == 5
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 6]) == 6
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 7]) == 7
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 8]) == 8
    assert test_game.getMatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == 9
