from bagels.bagels import Bagels


if __name__ == '__main__':
    game = Bagels(max_guesses=100, num_digits=10)
    game.run()
