class Button:               # class = ключевое слово создания классса

    def __init__(self, text, link):  #__init__ конструктор класса - стандартный метод объявления атрибутов
        self.text = text             # self = "коробочка", из которой достаются атрибуты
        self.link = link


#goHome = Button("","") вносим кнопку "гоухоум" в класс кнопка
#goHome.text

# Создаем экземпляры класса или объекты
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'имеет ссылку' + home.link) #текст будет "кнопка домой имеет ссылку ..."

print('\n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)




class ButtonTwo:
    def __init__(self, test, link, loc):
        self.text = text
        self.link = link
        self.loc = loc              #loc = локатор

    def click(self):         #метод click он помещает внутрь строки переменную
        return 'Клик по локатору - {}', format(self.loc)    #"клик по локатору - self.loc"
                                                    #format - функция чтоб положить переменную внутрь функции
# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click()) #тут печатается "Клик по локатору - self.loc"


