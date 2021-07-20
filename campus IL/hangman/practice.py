"""bricks = int(input('enter 3 digit number\n'))


pig3 = bricks % 10
bricks = bricks // 10
pig2 = bricks % 10
bricks = bricks // 10
pig1 = bricks % 10

print(pig1)
print(pig2)
print(pig3)

total = pig3 + pig2 + pig1
print(total // 3)
print(total % 3)
print(total % 3 == 0)



#print("He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3))


print('"Shuffle, Shuffle, Shuffle", say it together!\n Change colors and directions,\n Don\'t back down and stop the player! \n \tDo you want to play Taki?\n\tPress y\\n')"""

"""encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"

print(encrypted_message[-1:-57:-2])

sentence = input('enter a string\n')
the_letter = sentence.find('a')

print(sentence[0:the_letter] + sentence[the_letter:].replace('a', 'e'))


a_word = input('enter a word\n')
a_word = a_word.lower()
lenth = len(a_word)
if a_word[0:lenth+1] == a_word[::-1]:
    print('OK')
else:
    print('NOP')


temperature = int(input('enter a number\n'))
type = input("enter temp typy\('F', 'C')\n")
new_temp = str(temperature) + type
print(new_temp)
if type == 'F':
    temperature = temperature / 5
    print(str(temperature) + 'C')
else:
    temperature = temperature * 5
    print(str(temperature) + 'F')


import calendar

date = input('enter a date dd/mm/yyyy\n')
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])
print(calendar.weekday(year, month, day))"""

"""def last_early(my_str):
    if my_str[len(my_str) - 1] in my_str[0:len(my_str) -2]:
        return True
    else:
        return False
print(last_early('naama'))"""

"""def distance(num1, num2, num3):
    distance1_2 = abs(num1 - num2)
    distance2_3 = abs(num2 - num3)
    distance1_3 = abs(num1 - num3)
    if (distance1_2 ==  1 and distance1_3 == 1) or (distance2_3 >= 2 and distance1_2 >=2 and distance1_3 >= 2):
        return True
    else:
        return False
print(distance(1, 3, 6))"""

"""def fix_age(age):
    if 13 <= age <15 or 17 <= age <= 19:
        return 0
    else:
        return age

def filter_teens(a=13, b=13, c=13):
    teen_1 = fix_age(a)
    teen_2 = fix_age(b)
    teen_3 = fix_age(c)
    sum_ages = teen_1 + teen_2 + teen_3
    return sum_ages
print(filter_teens(12, 5, 6))


def chocolate_maker(small, big, x):
    big_choc = x / 5
    use_big = min(big_choc, big)
    use_big_cm = use_big * 5
    remaining_lenth = x - use_big_cm
    if small >= remaining_lenth:
        return True

    else:
        return False

print(chocolate_maker(10, 5, 50))"""

"""def main():


def func(num1, num2):
    if num1 > num2:
        return True
    else:
        return False
print(func(3, 5))"""

"""my_list = [1, 2, 3]
my_list.append(my_list[0])
my_list.remove(my_list[0])
print(my_list)"""

"""def shift_left(first, second, third):
    #this func taks 3 params and moves them 1 step to the left
    my_list = [first, second, third]
    my_list.append(my_list[0])
    my_list.remove(my_list[0])
    print(my_list)
shift_left('t', 2, 'wow')


def format_list(my_list):
    my_list = []
    print(my_list[::2])


format_list(my_list['hi', 'bye', 'hello', 'yay'])"""

#לבדוק עם איתי כשהוא יתפנה
"""def format_list(words_list):
    final_string = str()
    list1 = words_list[::2]
    for i in list1:
        final_string = final_string + i
    word = words_list[-1]
    print(final_string + ' and' + str(word))
format_list(['hi,', ' bey,', ' what,', ' why,', ' where,',' when'])"""


"""def extend_list_x(list_x, list_y):
    x = [1, 2, 3]
    y = [4, 5, 6]
    x[:0] += y
    print(x)
extend_list_x(x, y)"""



"""def are_lists_equal(list1, list2):
    x = sorted(list1)
    y = sorted(list2)
    if x == y:
        return True
    else:
        return False
print(are_lists_equal([0, 2.1, 3, 4,], [4, 3, 2.1, 1]))"""


"""def the_longest_word(my_list):
    longest_string = max(my_list, key=len)
    print(longest_string)
the_longest_word(['hikkkkjuj', 'bey', 'hello', 'morning'])"""

"""def squared_numbers(start, stop):
    numbers = []
    i = start
    while start <= i <= stop:
        numbers.append(i*i)
        i = i + 1
    return numbers
print(squared_numbers(10, 20))"""


"""def is_greater(my_list, n):
    new_list = []
    for num in my_list:
        if num > n:
            new_list.append(num)
    return new_list

print(is_greater([1, 2, 3, 4 ,5, 6], 4))"""

"""def numbers_letters_count(my_str):
    x = 0
    y = 0
    # new_list = []
    for i in my_str:
        if i.isdigit():
            x += 1
        else:
            y += 1
    # new_list.append(x)
    # new_list.append(y)
    return [x, y]
print(numbers_letters_count("hello 15")) """



































































