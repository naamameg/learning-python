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


#2.3.4
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

main()