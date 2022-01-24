import this


class test:
    'test'
    def __init__(self, name, mess):
        self.name = name
        self.mess = mess
    def say(self):
        print(self.name)


a = test("hello", {"age": 17})
# b = Atest("hello", {"age": 17})
a.say()