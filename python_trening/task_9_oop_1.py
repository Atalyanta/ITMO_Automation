class Input:                        # аргумент - это то, что в скобках у функции
    def __init__(self, loc, text):        #метод инициализации имеет 2 объектa
        self.loc = loc
        self.text = text
search = Input('печатай')       #cоздаем объект по классу инпут, и в этот объект передаем атрибут "печатай"
print(search.loc) # обращаемся к объекту, потом вызываем его атрибут. будет напечатано "печатай"


class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
modus = Button('кнопка')
print(modus.text, modus.loc)
class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
modus = Title('заголовок')
print(modus.text, modus.loc)
class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
modus = Link('ссылка')
print(modus.text, modus.loc)
