GUESE_A_LETTER = input('enter a letter\n')
if not GUESE_A_LETTER.isalpha() and len(GUESE_A_LETTER) > 1:
    print('E3')
elif len(GUESE_A_LETTER) > 1:
    print('E1')
elif not GUESE_A_LETTER.isalpha():
    print('E2')

else:
    print(GUESE_A_LETTER.lower())