class A:
    def __init__(self):   #
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()      #строка бывает только такая
        self.y = self.x + 5       # х берется из родительского класса

print(B().y)
b = B()
print(b.y)
