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


"""def seven_boom(end_number):

    numbers = []
    for number in range(end_number):
        if number % 7 == 0 or '7' in str(number):
            numbers.append('BOOM!')
        else:
            numbers.append(number)
    return numbers
print(seven_boom(10))"""



"""def sequence_del(my_str):
    y = ""
    for letter in range(len(my_str)):
        if my_str[letter] != my_str[letter-1]:
            y = y + my_str[letter]
    return y
print(sequence_del('hhhheeeeyyyyy'))"""



"""def menu():
    grocery_list = []
    list_1 = input('enter your list here\n').split(',')
    for word in list_1:
        grocery_list.append(word)
        number = 0
    while number != 9:
        number = int(input('enter a number between 1 and 9\n'))
        if number == 1:
            menu_option_1(grocery_list)
        elif number == 2:
            menu_option_2(grocery_list)
        elif number == 3:
            menu_option_3(grocery_list)
        elif number == 4:
            menu_option_4(grocery_list)
        elif number == 5:
            menu_option_5(grocery_list)
        elif number == 6:
            menu_option_6(grocery_list)
        elif number == 7:
            menu_option_7(grocery_list)
        elif number == 8:
            menu_option_8(grocery_list)
    print('Goodbye!')



#1
def menu_option_1(grocery_list):
    print(grocery_list)


#2
def menu_option_2(grocery_list):
    print('You have ' + str(len(grocery_list)) + ' item in your list')

#3
def menu_option_3(grocery_list):
    item = input('enter an item to check\n')
    if item in grocery_list:
        print('Item in grocery list')
    else:
        print('Item is not in grocery_list')

#4
def menu_option_4(grocery_list):
    user_item = input('enter item to check count in list\n')
    counter = 0
    for item in grocery_list:
        if item == user_item:
            counter +=1
    print('Item in list ' + str(counter) + ' times')

#5
def menu_option_5(grocery_list):
    user_item= input('enter an item to delete\n')
    grocery_list.remove(user_item)

#6
def menu_option_6(grocery_list):
    user_item = input('enter an item to add\n')
    grocery_list.append(user_item)

#7
def menu_option_7(grocery_list):
    not_legal_items = []
    for item in grocery_list:
        if len(item) < 3:
            not_legal_items.append(item)
        else:
            for letter in item:
                if not letter.isalpha():
                    not_legal_items.append(item)
                    break
    print(not_legal_items)

#8
def menu_option_8(grocery_list):
    new_list = []
    indexes_to_remove = []
    for index in range(len(grocery_list)):
        if not grocery_list[index] in new_list:
            new_list.append(grocery_list[index])
        else:
            indexes_to_remove.append(index)
    for i in range(len(indexes_to_remove)-1,-1,-1):
        del grocery_list[indexes_to_remove[i]]

menu()"""




"""def arrow(my_char, max_length):
    for i in range(1, max_length):
        new_char = my_char * i
        print(new_char)
    x = max_length
    for i in range(max_length, 0, -1):
        new_char = my_char * i
        print(new_char)
arrow('h', 3)"""

"""#ask etay
data = ("self", "py", 1.543)
format_string = "Hello", "learner, you have only", "units before you master the course!"
print(format_string[0] + ' ' + data[0] + ' ' + data[1] + ' ' + format_string[1] + ' ' + str(data[2])[:3] + ' '+ format_string[2])"""


"""def mult_tuple(tuple1, tuple2):
    empty_list = []
    for item in tuple1:
        for i in range(len(tuple2)):
            empty_list.append((item, tuple2[i]))
            empty_list.append((tuple2[1], item))
    empty_list = tuple(empty_list)
    return empty_list
print(mult_tuple((1,2,3),(4,5,6)))"""


"""def sort_anagrams(list_of_strings):
    used_words = []
    yet_another_empty_list = []
    empty_list= []
    for word in list_of_strings:
        word = list(word)
        word.sort()
        empty_list.append(word)
    for i in range(len(empty_list)):
        another_empty_list = []
        for j in range(len(empty_list)):
            if empty_list[i] == empty_list[j]:
                if not empty_list[j] in used_words:
                    another_empty_list.append(list_of_strings[j])
                    used_words.append(list_of_strings[j])
        yet_another_empty_list.append(another_empty_list)
    return yet_another_empty_list
print(sort_anagrams(['abc', 'cba']))"""



"""id_dict = {'firstname': 'Mariah', 'last name': 'Carey', 'birth date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}
def mariah_carey(my_dict):
    choose_number = int(input('enter a number between 1 and 7\n'))
    if choose_number == 1:
        print(my_dict['last name'])
    elif choose_number == 2:
        print(my_dict['birth date'])
    elif choose_number == 3:
        print(len(my_dict['hobbies']))
    elif choose_number == 4:
        print(my_dict['hobbies'][-1])
    elif choose_number == 5:
        my_dict['hobbies'].append('Cooking')
        print(my_dict)
    elif choose_number == 6:
        my_dict['birth date'] = my_dict['birth date'].split('.')
        my_dict['birth date'] = tuple(my_dict['birth date'])
        print(my_dict['birth date'])
    elif choose_number == 7:
        my_dict['age'] = '51'
        print(my_dict)
    return my_dict
mariah_carey(id_dict)"""


"""def count_chars(my_str):
    used_letters = []
    count_chars_dict = {}
    for letter in my_str:
        letters = 0
        if letter not in used_letters:
            for another_letter in my_str:
                if another_letter == letter:
                    letters = letters + 1
                count_chars_dict[letter] = letters
                used_letters.append(letter)
    return count_chars_dict
print(count_chars('I DID IT!!!!'))"""


"""def inverse_dict(my_dict):
    reverse_dict = {}
    for key, value in my_dict.items():
        value_list = [key]
        if value in reverse_dict:
            reverse_dict[value].append(key)
        else:
            reverse_dict[value] = value_list
    return reverse_dict

def not_even(a_dict):
    for key, value in a_dict.items():
        if value %2 != 0:
            print(key)

not_even({'a': 3, 'b': 2, 'c': 3})
# print(inverse_dict({'a': 3, 'b': 2, 'c': 3}))"""


"""def are_files_equal(file1, file2):
    file1 = open(file1)
    file2 = open(file2)
    content1 = file1.read()
    file1.close()
    content2 = file2.read()
    file2.close()
    if content1 == content2:
        return True
    else:
        return False
print(are_files_equal(r"C:\naama\files\a.txt", r"C:\naama\files\c.txt"))"""



"""def print_song():
    file = open(input('enter a file path\n'))
    task = input('enter a task: sort, rev or last\n')
    if task == 'sort':
        content = file.read()
        content = content.split(" ")
        content = sorted(content)
        print(content)
    elif task == 'rev':
        for line in file:
            print(line[-1::-1])
    elif task == 'last':
        number = int(input('enter a number\n'))
        count = file.readlines()
        print(count[number:])
    file.close()
print_song()"""


# def copy_file_content(source, destination):
#     with open(source, 'r') as source_file:
#         x = source_file.read()
#     with open(destination, 'w') as destination_file:
#         destination_file.write(x)
# copy_file_content(r"C:\Users\yuval\PycharmProjects\source.txt", r"C:\Users\yuval\PycharmProjects\destination.txt")



"""def list_from_file(file_path):
    with open(file_path, 'r') as handler:
        numbers_line = handler.read().split(',')
        for i in range(len(numbers_line)):
            numbers_line[i] = int(numbers_line[i])
    return numbers_line

def who_is_missing(file_name):
    numbers = list_from_file(file_name)
    numbers.sort()
    for i in range(len(numbers)):
        if numbers[i+1] - numbers[i] == 1:
            continue
        else:
            the_number = numbers[i + 1] - 1
            the_number = str(the_number)
            with open(r'found_number.txt', 'w') as new_file:
                new_file.write(the_number)
            break"""

"""def convert_to_seconds(time):
    time = time.split(":")
    minutes = int(time[0])
    seconds = int(time[1])
    total_time = minutes * 60 + seconds
    return total_time

def play_list(file_songs):
    song_dict = {}
    with open(file_songs, 'r') as handler:
        my_song_list = handler.read().split(";")
        my_song_list.remove(my_song_list[-1])
        for i in range(0, len(my_song_list), 3):
            if my_song_list[i][0] == "\n":
                my_song_list[i] = my_song_list[i][2:]
            song_dict[my_song_list[i]] = [my_song_list[i+1], convert_to_seconds(my_song_list[i+2])]
    return song_dict


def my_mp3_playlist(file_path):
    songs = play_list(file_path)
    longest_song_time = 0
    longest_song_name = ''
    number_of_songs = 0
    singer_names = {}
    most_song = ''
    number_of_singers = 0
    for song_name, song_details in songs.items():
        if song_details[0] in singer_names:
            singer_names[song_details[0]] = singer_names[song_details[0]] +1
        else:
            singer_names[song_details[0]] = 1
        number_of_songs = number_of_songs + 1
        if song_details[1] > longest_song_time:
            longest_song_time = song_details[1]
            longest_song_name = song_name
    for name, song in singer_names.items():
        if singer_names[name] > number_of_singers:
            number_of_singers = singer_names[name]
            most_song = name
    return (longest_song_name, number_of_songs, most_song)

print(my_mp3_playlist())"""


"""def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as songs:
        song_lines = songs.readlines()
        song_string = ''
        for i in range(len(song_lines)):
            if i == 2:
                song_lines[i] = new_song
            song_string = song_string + song_lines[i]

    with open(file_path, 'w') as destination_file:
        new_songs_list = destination_file.write(song_string)
my_mp4_playlist()"""





























































