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
print(try_update_letter_guessed('aa', ['t', 'r', 'o']))





