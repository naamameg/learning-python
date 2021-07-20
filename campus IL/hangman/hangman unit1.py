import random
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))


print("Wellcome to the game Hangman")
print(""" _    _
| |  | |
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |                    
                      |___/""")

print("x-------x")
print("""x-------x
|
|
|
|
|""")
print("""x-------x
|       |
|       0
|
|
|""")
print("""x-------x
|       |
|       0
|       |
|
|""")
print("""x-------x
|       |
|       0
|       |
|      /|\
|""")
print("""x-------x
|       |
|       0
|       |
|      /|\\
|      /""")
print("""x-------x
|       |
|       0
|       |
|      /|\\
|      / \\""")