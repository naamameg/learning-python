"""#2.2.2 + 2.3.3
class frog:
    count_animals = 0
    def __init__(self,age, name="frugo"):
        self._name = name
        self._age = age
        frog.count_animals +=1
    def birthday(self):
        self._age += 1
    def get_age(self):
        return self._age
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
def main():
    frog_1 = frog(5, "frogy")
    frog_2 = frog(7)
    frog_1.birthday()
    frog_2.set_name("friga")
    print(frog_1.get_age())
    print(frog_2.get_age())
    print(frog.count_animals)
    print(frog_1.get_name())
    print(frog_2.get_name())
main()"""


"""#2.3.4
class Pixel:
    def __init__(self, coordinate_1, coordinate_2, color_1=0, color_2=0, color_3=0):
        self._x = coordinate_1
        self._y = coordinate_2
        self._red = color_1
        self._green = color_2
        self._blue = color_3
    def set_coords(self, x, y):
        self._x = x
        self._y = y
    def set_grayscale(self):
        sum_colors = int((sum([self._red, self._green, self._blue])) / 3)
        self._red = sum_colors
        self._green = sum_colors
        self._blue = sum_colors
    def print_pixel_info(self):
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print (f"x: {self._x}, y: {self._y} color: ({self._red}, {self._green}, {self._green}) blue")
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            print (f"x: {self._x}, y: {self._y} color: ({self._red}, {self._green}, {self._green}) green")
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            print (f"x: {self._x}, y: {self._y} color: ({self._red}, {self._green}, {self._green} ) red")
        else:
            print(f"x: {self._x}, y: {self._y} color: ({self._red}, {self._green}, {self._green})")

def main():
    pixel_1 = Pixel(5,6,250,0,0)
    pixel_1.print_pixel_info()
    pixel_1.set_grayscale()
    pixel_1.print_pixel_info()

main()"""



#2.2.2

"""class Sparrow:
    count_animals = 0
    def __init__(self, age, name="octavio"):
        self._name = name
        self._age = age
        Sparrow.count_animals += 1
    def birthday(self):
        self._age += 1
    def get_age(self):
        return self._age
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

def main():
    sparrow_1 = Sparrow(4, "sparrow")
    sparrow_2 = Sparrow(6)
    print(sparrow_1.get_name())
    print(sparrow_2.get_name())
    sparrow_2.set_name("frogy")
    print(sparrow_2.get_name())
    print(Sparrow.count_animals)
    print(dir(Sparrow))
main()"""




"""def main():
    sparrow_1 = Sparrow(2, "sprey")
    sparrow_2 = Sparrow(4, "super")
    sparrow_1.birthday()
    print(sparrow_1.get_age())
    print(sparrow_2.get_age())
main()"""

"""#2.4.2
class BigThing:
    def __init__(self, word):
        self._word = word
    def size(self):
        if isinstance(self._word, int):
            return self._word
        elif isinstance(self._word, dict) or isinstance(self._word, list) or isinstance(self._word, str):
            return len(self._word)

class BigCat(BigThing):
    def __init__(self, word, weight):
        BigThing.__init__(self, word)
        self._weight = weight
    def size(self):
        super().size()
        if self._weight > 20:
            print("very fat")
        elif self._weight > 15:
            print("fat")

        else:
            print("OK")

def main():
    animal_1 = BigCat("pif", 76)
    animal_1.size()
    animal_2 = BigThing("lush")
    print(animal_2.size())
main()"""


#תרגיל מסכם
#2.5

class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name
    def __str__(self):
        return str(self._name) + str(self.__init_subclass__())
    def is_hungry(self):
        if self._hunger > 0:
            return True
    def feed(self):
        self._hunger -= 1
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")
    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        print("meow")
    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        self._stink_count = stink_count
        Animal.__init__(self, name, hunger=hunger)

    def talk(self):
        print("tssss")
    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")
    def sing(self):
        print("So call me, maybe")

class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        self._color = color
        Animal.__init__(self, name, hunger=hunger)

    def talk(self):
        print("Raaawr")
    def breath_fire(self):
        print("$@#$#@$")


def main():
    dog = Dog("Brownie", 10)
    dog1 = Dog("Doggo", 80)
    cat = Cat("Zelda", 3)
    cat1 = Cat("Kitty", 80)
    skunk = Skunk("Stinky", 0)
    skunk1 = Skunk("stinky jr", 80)
    unicorn = Unicorn("Keith", 7)
    unicorn1 = Unicorn("Clair", 80)
    dragon = Dragon("Lizzy", 1450)
    dargon1 = Dragon("McFly", 80)
    my_zoo = [dog, cat, skunk, unicorn, dragon]
    for animal in my_zoo:
        print(f"{type(animal).__name__} {animal._name}")
        animal.talk()
        if type(animal).__name__ == Dog:
            animal.fetch_stick()
        elif type(animal).__name__ == Cat:
            animal.chase_laser()
        elif type(animal).__name__ == Skunk:
            animal.stink()
        elif type(animal).__name__ == Unicorn:
            animal.sing()
        elif type(animal).__name__ == Dragon:
            animal.breath_fire()
    for animal in my_zoo:
        while animal.is_hungry():
            animal.feed()
    print(Dog.zoo_name)

main()



"""def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    my_zoo = [dog, cat, skunk, unicorn, dragon]
    class_list = ["Dog", "Cat", "Skunk", "Unicorn", "Dragon"]
    zoo_list = ["Brownie", "Zelda", "Stinky", "Keith", "Lizzy"]
    zoo_dict = dict(zip(class_list, zoo_list))
    for class_list,zoo_list in zoo_dict.items():
        print(class_list, zoo_list)
    for animal in my_zoo:
        while animal.is_hungry():
            animal.feed()


main()"""