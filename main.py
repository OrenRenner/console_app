from bagels.bagels import Bagels
from birthdayparadox.birthdayparadox import BirthdayParadox
import sys


if __name__ == '__main__':
    '''
    Usage: python main.py [bagels|birthdayparadox]
    '''
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'bagels':
            if len(sys.argv) == 3:
                bagels = Bagels(num_digits=int(sys.argv[2]))
            else:
                bagels = Bagels()
            bagels.run()
        elif sys.argv[1] == 'birthdayparadox':
            birthday_paradox = BirthdayParadox()
            birthday_paradox.run()
        else:
            print('Usage: python main.py [bagels|birthdayparadox]')
    else:
        print('Usage: python main.py [bagels|birthdayparadox]')
