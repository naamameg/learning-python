"""def combine_coins(coin_type, numbers):
    coin = ""
    for number in numbers:
        coin = coin + coin_type + str(number) + ", "
    return coin
print(combine_coins("$", [1, 2, 3, 4, 5]))
"""
import functools

"""#1.1.2
import functools

def double_letter(my_str):
    return my_str * 2
def add(a, b):
    return  a + b

print(functools.reduce(add, list(map(double_letter, "python"))))"""


"""#1.1.3
import functools
def four_dividers(number):
    return number % 4 == 0
print(list(filter(four_dividers,range(10))))"""

"""#1.1.4
import functools

def number_to_digit_list(number):
    numbers_list = []
    x = 0
    while number != 0:
        x = number % 10
        numbers_list.append(x)
        number = int(number / 10)
    return numbers_list

def add(a, b):
    return a + b
def sum_of_digits(number):
    return functools.reduce(add, number_to_digit_list(number))
print(sum_of_digits(201))"""


"""#1.2.1
a = lambda x: 1
print(a(3))
print(a("s"))
print(a(2))
print(type(a(3)))
"""


"""#אתגר המטבע
def combine_coins(coin_type, numbers):
    coin = ""
    for number in numbers:
        coin = coin + coin_type + str(number) + ", "
    return coin
print(combine_coins("$", [1, 2, 3, 4, 5]))

import functools
def add(a,b):
    return a + b

def combine_coins_2 (coin_type, numbers):
    return functools.reduce(add, [coin_type + str(numbers[i]) + " " for i in range(len(numbers))])
print(combine_coins_2("$", [1, 2, 3, 4, 5]))"""



"""#1.3.1
import functools

def intersection(list_1, list_2):
    return list(filter(lambda x: x in list_1 and x in list_2, list_1 + list_2))
print(functools.reduce(intersection([1, 2], [2, 3])))

def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))
print(intersection([2, 2, 1], [1, 2, 3]))

set1 = {1,2}
set2 = {2,3}
print(set1.intersection(set2))
"""

"""return lambda x: for i in range(2, number) if (number % i) == 0
print(is_prime(15))"""

#1.3.2
"""def is_prime_1(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    return True

print(is_prime_1(12))"""

"""def is_prime(number):
    return len([i for i in range(2, number) if (number % i) == 0]) == 0
print(is_prime(23))"""


#1.3.3

"""def is_fun(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True"""

"""def is_funny(string):
    return len([x for x in string if x != 'a' and x != 'h']) == 0

print(is_funny("hahaha"))"""



#משימה מסכמת
import functools

"""
def long_name(file_path):
    with open(file_path,'r') as names_list:
        names_list = names_list.read().split("\n")
        print(max(names_list))
"""
"""def longest_name(file_path):
    with open(file_path, 'r') as names:
        return functools.reduce(max, names)"""


def add(num1, num2):
    return num1 + num2

"""def total_names(file_path):
    with open(file_path, 'r') as names:
        names_list = names.read().split()
        len_list = [len(word) for word in names_list]
        return functools.reduce(add, len_list)"""


"""def total_names(file_path):
    with open(file_path, 'r') as names:
        return functools.reduce(lambda num1, num2: num1 + num2, [len(word) for word in names.read().split()])"""


"""def shortest_word(file_path):
    with open(file_path, 'r') as names:
        names_list = names.read().split()
        list_1 = sorted(names_list, key=len)
        return [list_1[i] for i in range(len(list_1)-1) if len(list_1[i]) == len(list_1[0])]"""


def write_length_file(file_path):
    with open(file_path, 'r') as handler:
        names_list = handler.read().split()
    with open("names_file.txt", 'w') as new_file:
        new_names_list = new_file.write(str([str(len(word)) for word in names_list]))
write_length_file(r"C:\Users\naama\python studies\learning-python\names.txt.txt")

