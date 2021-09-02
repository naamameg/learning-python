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


"""def get_a_dict(number):
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


def check_win(secret_word, old_letters_guessed):"""

"""people_dict = {'204323877': {'name': 'naama', 'quest': 'learning python', 'favorite color': 'blue'},
               '314010521':{'name': 'etay', 'quest': 'teaching python', 'favorite color': 'black'}}
people_dict['204323877']['last name'] = 'megidish'


dict_of_nums = {1: 'hello', 2: 'bye', 3 : 'what why'}

for key, value in dict_of_nums.items():
    print(f"the value of key {key} is {value}")"""




#1
#קבלי רשימה של מספרים, והדפיסי רשימה שכל איבר בה הוא פי 2 מהאיבר המתאים ברשימה שקיבלת

"""def double_number(num):
    return num * 2
list1 = [1,2,3,4,5]
result = list(map(double_number, list1))
print(result)"""

"""def double_number(a_list):
    return [x*2 for x in a_list]
print(double_number([1,2,3,4,5]))"""


#2
#קבל רשימה של מספרים והדפיסי רשימה שיש בה רק את הזוגיים מביניהם

"""def even_number(num_list):
    return [x for x in num_list if x % 2 ==0]
print(even_number([1,2,3,4,5,6,7,8,9]))"""


#3
#קבלי רשימה של מספרים והדפיסי רשימה שכל איבר בה הוא פי 2 מאיבר אי זוגי ברשימה שקיבלת

"""def double_odd_nuber(num_list):
    return [x * 2 for x in num_list if x % 2 != 0]
print(double_odd_nuber([1,2,3,4,5,6,7,8,9]))"""


"""#4
#קבלי רשימה של מחרוזות. הדפיסי רשימה שכל איבר בה הוא האיבר המתאים ברשימה שקיבלת, רק שאחריו כתוב גם "please"

def please(words_list):
    return [word + " please" for word in words_list]
print(please(['what?', 'why?']))
"""

"""#1
#לקבל רשימה של מחרוזות ולהדפיס את האות הראשונה של כל איבר ברשימה שמורכב מ 10 תווים או פחות
def ten_letters(string_list):
    return [word[0] for word in string_list if len(word) < 10]
print(ten_letters(['hello', 'asdfghjkzx', 'name', 'rjhutkgivun']))
"""
"""#2
#לקבל רשימה ולהדפיס רשימה שיש בה רק את האיברים במקומות הזוגיים ברשימה שקיבלת (כלומר את המקום ה 0, המקום ה 2 וכו')

def even_word(words):
    return [words[i] for i in range(len(words)) if i %2 ==0]
print(even_word(['hello', 'asdfghjkzx', 'name', 'rjhutkgivun']))"""

#3
#לקבל שתי רשימות של מספרים ולהדפיס רשימה שיש בה רק את האיברים ברשימת קלט א שגדולים יותר מכלל האיברים ברשימה השניה (נניח אם האיבר המקסימלי ברשימה השניה הוא 7, אז להדפיס רק איברים שגדולים מ 7 מהרשימה הראשונה)

"""def bigger_number_list(num_list_1, num_list_2):
    return [num for num in num_list_1 if num > max(num_list_2)]
print(bigger_number_list([1,2,3,4,5,6],[1,2,3]))"""

"""#4
#לקבל רשימה של מספרים ולהדפיס רשימה של המספרים ההופכיים (כלומר אם המספר הוא 3 אז ברשימת הפלט יהיה מינוס 3, ואם המספר הוא מינוס 3 אז יהיה ברשימת הפלט 3)

def opposite_number(num_list):
    return [-num for num in num_list]
print(opposite_number([1,2,3,4,-5]))"""

"""#5
#לקבל מחרוזת של ספרות ולהדפיס רשימה שכל איבר בה הוא מספר ששווה לספרה שיש למחרוזת במקום המתאים

def positinn_number(number_string):
    return [int(digit) for digit in number_string]
print(positinn_number("123"))"""


class Clock:

    def __init__(self, corrent_time):
        self._corrent_time = corrent_time
        self.TIMEZONES = {
            "jerusalem": 3,
            "New Yort": -2,
            "Milano": 0
        }
    def time_passes(self, houres):
        self._corrent_time = (self._corrent_time + houres) % 24
    def print_time(self, TIMEZONE="Milano"):
        new_time = (self._corrent_time + self.TIMEZONES[TIMEZONE])
        print(new_time)
        if new_time >= 20:
            print("good night")

time = Clock(7)
time_shtaim = Clock(7)
time.time_passes(8)
time.print_time(TIMEZONE="jerusalem")
time_shtaim.print_time()









