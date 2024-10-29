class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.pointer = start
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise StepValueError()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        self.sign = self.step/abs(self.step)
        if self.sign > 0 and (self.pointer > self.stop or self.pointer < self.start):
            raise StopIteration()
        elif self.sign < 0 and (self.pointer > self.start or self.pointer < self.stop):
            raise StopIteration()
        else:
            return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()