class Dog:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = 'Woof!'

    def say(self):
        return self.sound


class Cat:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = 'Meow!!'

    def say(self):
        return self.sound


def creare_pet(nickname, pet='dog'):                 # ця функція фактично є фабрикою. Патерн фабрика повинен створювати
    pets = dict(dog=Dog(nickname), cat=Cat(nickname))  # екземпляри класу. Ця функція створює екземпляр класу в залежності
    print(pets)                                        # від того що їй передається
    return pets.get(pet)


if __name__ == '__main__':
    d = creare_pet('Bobic')
    print(d.say())
    m = creare_pet('Tom', 'cat')
    print(m.say())
