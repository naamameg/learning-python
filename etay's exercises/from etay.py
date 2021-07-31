#1

"""def create_snake(number):
    snake = ['head',]
    x = int(number) * 'body,'
    x = x.split(',')
    for num in x[:-1]:
        snake.append(num)
    snake.append('tail')
    return snake
print(create_snake(3))"""


#2

"""def count_snake(snake):
    counter = 0
    for body in snake[1:-1]:
        counter += 1

    return counter
print(count_snake(['head', 'body', 'body', 'tail']))"""

#3
"""x = {'g': 1, 'd': 3}
print('ggg' in x)



def dicts(dict_1, dict_2):
    values = []
    for key in dict_1:
        if key in dict_2:
            values.append(dict_1[key])
            values.append(dict_2[key])
        return values
print(dicts({"a": 1, "b": 2}, {"a": 3, "c": 4}))"""


#4

"""def devided_by_two():
    user_number = int(input('enter a number\n'))
    x = 0
    while user_number % 2 == 0:
        user_number = user_number / 2
        x += 1
    return x
print(devided_by_two())"""


"""def devided_by_two(number):
    x = 0
    while number % 2 == 0:
        number = number / 2
        x += 1
    return x
print(devided_by_two(8))

#5

def two_numbers(num1, num2):
    multi = num1*num2
    devision = num1 / num2
    defrence =num1 -num2
    print(devided_by_two(multi))
    print(devided_by_two(devision))
    print(devided_by_two(defrence))
two_numbers(5, 7)"""

#6

"""def my_string(a_string):
    letters = ''
    numbers = ''
    for index in a_string:
        if index.isalpha():
            letters = letters + index
        else:
            numbers = numbers + index
    numbers = numbers[-1::-1]
    print(letters)
    print(numbers)
my_string('gt6g6i1g253f')"""

#7

def list_in_dict(my_list):
    my_dict = {}
    if len(my_list) % 2 > 0:
        print('ERROR!!!!!!!!')
        return False
    else:
        for i in range(len(my_list)-1):
            if i % 2 == 0:
                my_dict[my_list[i]] = my_list[i+1]
        return my_dict



#1 extra

"""def two_num_function(num_1, num_2):
    my_dict_1 = {}
    my_dict_1[max(num_1, num_2)] = min(num_1, num_2)
    return my_dict_1
print(two_num_function(8, 9.))

#2 extra

d = {1: 5, 2: 'two', 3: {'naama': 'the queen'}}"""


#8

"""def in_dict(my_list):

    if len(my_list) % 2 > 0:
        print('ERROR!!!!!!!!')
        return False
    else:
        my_list = my_list[:-1].split(" ")
        return list_in_dict(my_list)
print(in_dict('a b c d '))"""


def get_a_dict(number):
    my_fucking_dick = {}
    for i in range(number):
        key = input('enter a key\n')
        value = [input('enter a value\n')]
        if key in my_fucking_dick:
            my_fucking_dick[key].extend(value)
        else:
            my_fucking_dick[key] = value
    return  my_fucking_dick
print(get_a_dict(2))


def check_win(secret_word, old_letters_guessed):






































