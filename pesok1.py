from pesok2 import B


class A:

    def __init__(self, name):
        self.name = name

    def func1(self):
        print('abc')


a = A(A)

a.func1()
A.func1(a)

# b = B()
#
# b.func2()
# B.func2(b)
