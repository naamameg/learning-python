"""def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


n = [1, 2, 5, 10, 13]
print(sum(n))

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)"""

"""student = {'names': 'John', 'age': 25, 'courses': ['Math', 'CompuSci']}
student.pop('age')
print(student)"""


"""#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    plus_middle = []
    for i in range(len(a)):
        if i == 1:
            plus_middle.append(a[1])
    for i in range(len(b)):
        if i == 1:
            plus_middle.append(b[1])
    return plus_middle
print(middle_way([1, 2, 3], [4, 5, 6]))

"""

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.

"""def make_ends(nums):
    first_end = []
    first_end.append(nums[0])
    first_end.append(nums[-1])
    return first_end

print(make_ends([1,2,3,4,5,6]))"""

"""#הפונקציה מקבלת מחרוזת ומחזירה מילון שכל מפתח הוא אות והערך הוא כמה מופעים יש לאות הזאת המחרוזת
def char_freq(a_string):
    freq = {}
    for letter in a_string:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] = freq[letter] + 1
    return freq
print(char_freq("naama"))"""



"""#this function
def encode_letter(letter):
    a = ""
    z = ""
    coded_letter_lower = (ord(letter) - ord('a') + 13) %(ord('z') + 1 - ord('a')) + ord('a')
    coded_letter_upper = (ord(letter) - ord('A') + 13) % (ord('Z') + 1 - ord('A')) + ord('A')
    if letter.islower():
        letter = coded_letter_lower
        letter = chr(letter)
    elif letter.isupper():
        letter = coded_letter_upper
        letter = chr(letter)
    return letter


def decode_letter(letter):
    coded_letter_lower = (ord(letter) - ord('a') - 13) % (ord('z') + 1 - ord('a')) + ord('a')
    coded_letter_upper = (ord(letter) - ord('A') - 13) % (ord('Z') + 1 - ord('A')) + ord('A')
    if letter.islower():
        letter = coded_letter_lower
        letter = chr(letter)
    elif letter.isupper():
        letter = coded_letter_upper
        letter = chr(letter)
    return letter



def encode_word(string):
    encoded_word = ""
    for letter in string:
        letter = encode_letter(letter)
        encoded_word = encoded_word + letter
    return encoded_word



def decode_word(code):
    decoded_word = ""
    for letter in code:
        if letter.isalpha():
            letter = decode_letter(letter)
            decoded_word = decoded_word + letter
        elif letter.isspace():
            decoded_word = decoded_word + letter
    return decoded_word
print(decode_word('v nz yrneavat jvgu fur pbqrf npnqrzl!'))"""


"""def if_same_letter(list_1):
    same_letter = []
    for word in list_1:
        if word[0] == word[-1]:
            same_letter.append(word)
    return same_letter
print(if_same_letter(['aba', 'abb', 'ana', 'abc']))"""

"""#הפונקציה מקבלת 2 מחרוזות, ובודקת בכמה מקומות יש שני אינדקסים שנראים אותו דבר
def string_match(str_1, str_2):
    string = 0
    for i in range(len(str_1)-1):
        if str_1[i] == str_2[i] and str_1[i+1] == str_2[i+1]:
                string += 1
    return string
print(string_match("aabbcd", 'aabccc'))"""



"""#this function prints * equal to the number from 1 to the number
def pyramid_from_stars(number):
    star = ""
    for i in range(number):
        star = star + "*"
        print(star)
print(pyramid_from_stars(8))"""

"""#הפונקציה מקבלת מספר מהמשתמש, ומדפיסה כוכבים במספר עולה ב1
def trapezoid_from_stars():
    number = int(input('enter a numbe grater then 4\n'))
    star = ""
    for i in range(number):
        star = number * "*"
        print(star)
        number += 1
trapezoid_from_stars()
"""

"""ask etay
def diamond_from_stars(number):
    star = ""
    for i in range(number):
        star = star + "*"
        print(star)
        while len(star) == number:
            star = star - "*"
            print(star)

diamond_from_stars(6)"""


"""import random
def guess_a_number():
    numbers_list = list(range(1, 11))
    number = int(input("enter a number between 1 and 10\n"))
    random_number = random.choice(numbers_list)
    while number != random_number:
        if number > random_number:
            print("big")
            number = int(input("enter a number between 1 and 10\n"))
        elif number < random_number:
            print("small")
            number = int(input("enter a number between 1 and 10\n"))
    print("WIN")

guess_a_number()"""


"""for i in range(1, 51):
    if i % 7 == 0:
        print("BOOM")
    else:
        print(i)"""



"""def seven():
    for i in range(1, 21):
        number = input("enter a number\n")
        if i % 7 == 0:
            if number != "boom":
                print("LOSE")
                return False
            else:
                continue
        elif i % 7 != 0:
            if int(number) != i:
                print("LOSE")
                return False

    print("WIN")
    return True"""



"""def seven_boom():
    divided_by_7 = False
    divided_by_14 = False
    computer_turn = False
    for i in range(1, 51):
        computer_turn = i % 2 == 0
        divided_by_7 = i % 7 == 0
        divided_by_14 = i % 14 == 0
        if computer_turn:
            if not divided_by_7:
                print(i)
            elif divided_by_14:
                print(" boom trach")
            elif divided_by_7:
                print("boom")
        else:
            number = input("enter a number\n")
            if not divided_by_7:
                if int(number) != i:
                    print("LOSE")
                    return False
            elif divided_by_14:
                if number != "boom trach":
                    print("LOSE")
                    return False
            else:
                if number != "boom":
                    print("LOSE")
                    return False
seven_boom()"""


"""def name_movie(movies, names):
    name_and_movie = dict(zip(movies, names))
    return [f"{movie} is played by {name}" for movie,name in name_and_movie.items()]


print(name_movie(['A', 'B', 'C'], ['a', 'b', 'c']))
"""


"""def name_movie(movies, names):
    return dict(zip(movies, names))


print(name_movie(['A', 'B', 'C'], ['a', 'b', 'c']))"""

"""numbers = [i*100 for i in range(1,10) if i%2 == 0]
print(numbers)
"""

"""print([i*100 if i%2 == 0 else i for i in range(1,10)])"""

"""print(["boom" if i % 7 == 0 else i for i in range(1,51)])"""


"""even = list(map(lambda x: x * 100, filter(lambda y: (y%2 == 0), [1,2,3,4,5,6,7,8])))
print(even)

even_and_odd = list(map(lambda x: x*100 if x%2 == 0 else x, [1,2,3,4,5,6,7,8,9]))
print(even_and_odd)"""


"""seven_boom = list(map(lambda x: "boom!" if x%7 == 0 else x, range(1,51)))
print(seven_boom)
"""


"""from functools import reduce

sum = lambda x,y: x + y
print(sum(1,2))
"""

"""tuples = [(i,s) for i in range(1,7) for s in range(1,7)]
print(tuples)"""

"""joules = [1000,2000,3000,4000]
joule_to_kilo = list(map(lambda x: (x, x/4184), joules))
print(joule_to_kilo)


languages = ['a', 'b', 'c', 'Python']
find_python = [name for name in languages if name == "Python"]
print(find_python)"""


"""def anagram(word_1, word_2):
    x = -1
    for i in range(len(word_1)):
        if word_1[i] == word_2[x]:
            x -= 1
        else:
            return False
        return True

print(anagram("naama", "amaan"))"""




def roman_number(roman_digit):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50}
    x = 0
    for i in range(len(roman_digit)-1):
        if roman_digit[i] in roman_dict:
            if roman_digit[i] == "I" and roman_digit[i+1] != "I":
                x = x + (roman_dict[roman_digit[i]])
            else:
                x = x + roman_dict[roman_digit[i]]

    return x
print(roman_number("LX"))









