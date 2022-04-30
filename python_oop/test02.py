class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m
        print('self is {0} @A.add'.format(self))


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        print('self is {0} @B.add'.format(self))
        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        print('self is {0} @C.add'.format(self))
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        print('self is {0} @D.add'.format(self))
        self.n += 5


if __name__ == "__main__":
    d = D()
    d.add(2)
    print(d.n)
    print("hello")
    print("test")
