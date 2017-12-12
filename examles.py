
class Adder:
    def __init__(self):
        self.summa = None

    def add(self, x, y):
        assert False, 'Not implemented!'

class ListAdder(Adder):
    def add(self, x, y):
        self.summa = x + y
        print('Concatenated lists is', self.summa)


class DictAdder(Adder):
    def add(self, x, y):
        self.summa = x
        self.summa.update(y)
        print('Concatenated dict is', self.summa)



if __name__ == '__main__':
    #a = Adder()
    #a.add([1,2,3],[4,5,6])

    b = ListAdder()
    b.add([1, 2, 3], [4, 5, 6])

    c = DictAdder()
    c.add({'eggs': 3, 'ham': 1, 'spam': 2}, {'b': 2})
