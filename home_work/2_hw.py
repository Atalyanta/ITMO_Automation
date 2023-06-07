def task_1(): -> None:
    per1: int = 1
    per2: float = 1.1
    per3: 'абвгд'
    per4 = ['abc', 'efg']
    per5 = True
print(type(per1), type(per2), type(per3), type(per4), type(per5))


def task_2() -> None:
    d = [1, 2, 3, 5, 8, 13, 21]
print('d[0:3] = ', d[0:3])

def task_3(b: int) -> int:
    return b**2
print(task_3())

