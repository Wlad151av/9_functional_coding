
from random import choice

# Lambda function

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda a,b: a == b,first,second)))

# Замыкание переменных


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'w') as fn:
            for line in data_set:
                fn.write(str(line))
                fn.write('\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__
from random import choice
class MysticBall:
    def __init__(self,*args):
        self.words = []
        for word in args:
            self.words.append(word)

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Возможно', 'Отнюдь', 'Наверное' , 'А то!')
print(first_ball())
print(first_ball())
print(first_ball())
