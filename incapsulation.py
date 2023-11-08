class Animal:
    def __init__(self, name):
        self.name = name
        self.__head = 1
        self.__wing = 0

    def get_head_count(self):
        return self.__head

    def set_head_count(self, count):
        self.__head = count

    @property
    def wing(self):
        return self.__wing

    @wing.getter
    def wing(self):
        return self.__wing

    @wing.setter
    def wing(self, count):
        self.__wing = count

    def eat(self, food_count):
        if food_count > 1:
            print(f"{self.name} больше не голоден")
        else:
            print(f"{self.name} все еще хочет кушать")

    @staticmethod
    def say_smtn(paw_count):
        if paw_count > 2:
            print("Это животное")
        else:
            print("Это птица?")

    @classmethod
    def create_cat_with_class_method(cls):
        name = "Классный"
        cls(name=name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.paws = 4
        self.tail = 1

    def say_smtn(self):
        print(f"{self.name} says: Meow!")

    def change_name(self, new_name):
        self.name = new_name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.paws = 4
        self.tail = 1

    def say_smtn(self):
        print(f"{self.name} says: Wof!")


if __name__ == "__main__":
    animal = Animal("any")
    print(animal.wing)
    animal.wing = 2
    print(animal.wing)
    animal.set_head_count(2)
    animal._Animal__head = 3
    print(animal._Animal__head)
