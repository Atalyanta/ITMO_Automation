                    # if a>0
                    # elif a == 0
                    # else

num_float = -4.5

                # Также попробуйе варианты
                # num_float = 0
                # num_float = -4.5

if num_float >0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

            # иф а ор б: выполняется только когда и а, и б тру

                    # если пермит_принт тру и число больше 0 = иф, если перм_принт фолс = елиф
num = 0
permit_print = False
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

         # 1-4 курс бакалавр, 5-6 агистр, 79-аспирант, если не соотв "введите корректнй год"

kurs=10
if kurs in range(1,5):
    print('бакалавр')
elif kurs in range(5-6):
    print('магистр')
elif kurs in range(7-9):
    print('аспирант')
else:
    print('Введите корректный год обучения')


            # дано число, если оно больше 100 или меньше -100, вывести "-", иначе вывести "+"
a=-1000
if a in range(-100,100):
    print('+')
else:
    print('-')
                # или так:
if a>100 or a<-100:
    print('-')
else:
    print('+')



