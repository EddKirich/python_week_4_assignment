class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        pass

    def introduce(self):
        print(f"Hello. my name is {self.name}. I am {self.age} years old, and my gender is {self.gender}.")

person1 = Person("Edmond", 27, "male")

person1.introduce()