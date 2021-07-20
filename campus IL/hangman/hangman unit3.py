GUESE_A_LETTER = input('enter a letter\n')
print(GUESE_A_LETTER.lower())

ENTER_A_WORD = input('enter a word\n')


print(ENTER_A_WORD.replace(ENTER_A_WORD[:], '_'*len(ENTER_A_WORD)))