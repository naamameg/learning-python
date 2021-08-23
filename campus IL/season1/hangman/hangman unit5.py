def is_valid_input(letter_guessed):
    """"this function checks the input. if the input is not a letter' it returns false
    param letter_guessed: represent the input letter """

    if not letter_guessed.isalpha() and len(letter_guessed) > 1:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False

    else:
        return True
print(is_valid_input('i9'))