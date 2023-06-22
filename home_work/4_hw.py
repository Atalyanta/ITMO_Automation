                        #1
class Pryamougolnik:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def ploshad(self, width, height):
        return width*height
        print("Площадь", ploshad())
    def perimetr(self, width, height):
        return width+height+width+height
        print("Периметр", perimetr())


obj1 = Pryamougolnik(2, 3)
obj1.ploshad()
obj1.perimetr()


                                #2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        return a+b
        print(addition())

    def multiplication(self, a, b):
        return a*b
        print(multiplication())

    def division(self, a, b):
        return a/b
        print(division())

    def subtraction(self, a, b):
        return a-b
        print(subtraction())

                        #3
class Elements:
    type: str = "Кнопка"

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
    def click(self):
        return "Клик по локатору - {}".format(self.loc)

TextBox = Elements('TextBox')
print(TextBox.click())
CheckBox = Elements('CheckBox')
print(Checkbox.click())
RadioButton = Elements('RadioButton')
print(RadioButton.click())
            #и т.д.