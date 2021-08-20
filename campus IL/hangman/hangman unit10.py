#1
def print_title():
    print(""" _    _
| |  | |
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |                    
                      |___/""")

#2
def choose_word(file_path, index):
    words_list = 0
    dict_of_words = {}
    with open(file_path, 'r') as handler:
        word_to_choose_from = handler.read().split(" ")
    for word in word_to_choose_from:
        if word not in dict_of_words:
            dict_of_words[word] = 1
        else:
            dict_of_words[word] += 1
    for word in dict_of_words.keys():
        words_list += 1
    chosen_word = word_to_choose_from[(index-1) % len(word_to_choose_from)]
    return (words_list, chosen_word)

#3
HANGMAN_PHOTOS = {0: "x-------x", 1: "x-------x\n\
|\n\
|\n\
|\n\
|\n\
|", 2: "x-------x\n\
|       |\n\
|       0\n\
|\n\
|\n\
|", 3: "x-------x\n\
|       |\n\
|       0\n\
|       |\n\
|\n\
|", 4: "x-------x\n\
|       |\n\
|       0\n\
|       |\n\
|      /|\\\n\
|", 5: "x-------x\n\
|       |\n\
|       0\n\
|       |\n\
|      /|\\\n\
|      /", 6: "x-------x\n\
|       |\n\
|       0\n\
|       |\n\
|      /|\\\n\
|      / \\"}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

#4
def show_hidden_word(secret_word, old_letters_guessed):
    word_to_print = str()
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_to_print = word_to_print + (letter + ' ')
        else:
            word_to_print = word_to_print + ('_ ')
    print(word_to_print)

#5
def check_valid_input(letter_guessed, old_letters_guessed):
    if not letter_guessed.isalpha() and len(letter_guessed) > 1:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        new_old_letters_guessed = str()
        for i in old_letters_guessed[0:-1]:
            new_old_letters_guessed = new_old_letters_guessed + i + ' -> '
        if not old_letters_guessed:
            print("\n")
        else:
            print(new_old_letters_guessed + old_letters_guessed[-1])
        return False



#6

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if not letter in old_letters_guessed:
            return False
    return True


print_title()
number_of_tries = 0
print_hangman(number_of_tries)
file_path = input("enter a file path\n")
index = int(input('enter a number\n'))

secret_word = choose_word(file_path, index)
secret_word = secret_word[1]
old_letters_guessed = []


while not check_win(secret_word, old_letters_guessed):
    show_hidden_word(secret_word, old_letters_guessed)
    letter_to_choose = input('enter a letter\n')
    while not try_update_letter_guessed(letter_to_choose, old_letters_guessed):
        print("try again")
        letter_to_choose = input('enter a letter\n')
    if number_of_tries == 6:
        print("You'reeeee A Loser!")
        break
    elif letter_to_choose not in secret_word:
        print("):")
        print_hangman(number_of_tries + 1)
        number_of_tries +=1
if check_win(secret_word, old_letters_guessed):
    print(secret_word)
    print("You Win")



