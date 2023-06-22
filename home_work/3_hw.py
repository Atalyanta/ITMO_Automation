                                #2
def task2(a, b):
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else:
        print('Числа равны')

                                #3

def task3(a, b):
    if a-b==135 or b-a==135:
        print('yes')
    else:
        print('No')

                                #4
def task4(month):
    if month in range(3,6):
        print('весна')
    elif month in range(6,9):
        print('лето')
    elif month in range(9,12):
        print('осень')
    elif month in range(1-3) or 12:
        print('зима')
    else:
        print('Введите корректный номер месяца')


                                #5
def task5(a, b, c):
    if a>10 and b>10 and c>10:
        print('yes')
    else:
        print('no')
