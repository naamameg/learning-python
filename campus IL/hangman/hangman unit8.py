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
print_hangman(4)


x = ""