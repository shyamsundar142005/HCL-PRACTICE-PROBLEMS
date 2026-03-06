# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age= age
#
# def display(self):
#     print(self.name)
#     print(self.age)
# s1=student("shyam",25)
# display(s1)

# class student:
#     def __init__(self):
#         self.__balance=5000
#         print(self.__balance)
# s1=student()

# class animal:
#     def speak(self):
#         print("Animal speaks")
# class dog(animal):
#     def bark(self):
#         print("Dog barks")
# d=dog()
# d.speak()
# d.bark()

from abc import ABC,abstractmethod
class Payment_Gateway(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def refund(self):
        pass
    @abstractmethod
    def cancel(self):
        pass
