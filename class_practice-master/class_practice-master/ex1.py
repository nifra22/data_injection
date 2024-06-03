#Realization relationship between classes
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"
    def move(self):
        return "run"

class Bird(Animal):
    def make_sound(self):
        return "Chirp"
    def move(self):
        return "fly"

def main():
    animals = [Dog(), Bird()]

    for animal in animals:
        print(f"{animal.__class__.__name__} make sound: {animal.make_sound()} and move")
if __name__ == "__main__":
    main()

'''from abc import ABC, abstractmethod

class Students(ABC):
    @abstractmethod
    def student_pass(self):
        pass
    @abstractmethod
    def student_fail(self):
        pass

class Assignment(Students):
    def student_pass(self):
        return "Student is passed in Assignment"

    def student_fail(self):
        return "Student is failed in Assignment"

class Viva(Students):
    def student_pass(self):
        return "Student is passed in Viva"
    def student_fail(self):
        return "Student is failed in Viva"

def main():
    Students = [Assignment(), Viva()]

    for students in Students:
        print(f"{students.__class__.__name__} student_pass: {students.student_pass()} and student_fail")

if __name__ == "__main__":
    main()'''



