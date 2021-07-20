HANGMAN_ASCII_ART = "Wellcome to the game Hangman \n \
 _    _\n \
| |  | |\n \
| |  | |\n \
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n \
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n \
| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n \
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n \
                       __/ |                    \n \
                      |___/"

import random
list1 = [1, 2, 3, 4, 5, 6]
MAX_TRIES = random.choice(list1)
print(HANGMAN_ASCII_ART)
print(random.choice(list1))


GUESE_A_LETTER = input('enter a letter\n')
print(GUESE_A_LETTER)