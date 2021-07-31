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
        print(new_old_letters_guessed + old_letters_guessed[-1])
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    word_to_print = str()
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_to_print = word_to_print + (letter + ' ')
        else:
            word_to_print = word_to_print + ('_ ')
    print(word_to_print)

show_hidden_word('helli', ['l', 'r', 'q', 'x'])

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if not letter in old_letters_guessed:
            return False
    return True
print(check_win('hello', ['l', 'e', 'h', 'o', 'r']))

















