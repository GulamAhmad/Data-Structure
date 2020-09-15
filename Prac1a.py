class list_fun:
    def __init__(self):
        self.l = []

    def adding(self,n):
        self.l.append(n)

    def searching(self,f):
        if f in self.l:
            print("found!!")
        else:
            print("not found")

    def sorting(self):
        self.l.sort()

    def reversing(self):
        self.l = self.l[::-1]

    def display(self):
        print(self.l)

l1 = list_fun()
l1.adding(8)
l1.adding(3)
l1.adding(4)
l1.adding(1)
l1.adding(9)
l1.adding(2)

l1.searching(3)
l1.sorting()
l1.display()
l1.reversing()
l1.display()
