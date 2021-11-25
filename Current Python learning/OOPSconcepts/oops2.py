# class Calculator:
#     def __init__(self, anum1, anum2):
#         self.num1 = anum1
#         self.num2 = anum2
#
#     def add(self):
#         return self.num1 + self.num2
#
#
# addition = Calculator(3, 4)
# print(addition.add())


# # ---- CAR Details ----
class CarDetails:
    def __init__(self, car, model, colour, company):
        self.aowner = car
        self.amodel = model
        self.acolour = colour
        self.acompany = company

    def details(self):
        print(f"Owner: {self.aowner}\n"
              f"Model: {self.amodel}\n"
              f"Colour: {self.acolour}\n"
              f"Company: {self.acompany}\n")


car1 = CarDetails("Liyakhat yousuf mogal", "Sedan", "Red", "Hyundai")
car2 = CarDetails("Harry Bhai", "Suv", "Blue", "BMW")
car1.details()
car2.details()

# # =================================================

# class Palindrome:
#     n = ""
#     def palindrome(self, n):
#         reverse = ""
#         for i in n:
#             reverse = i + n
#         if reverse == n:
#             print(f"{n} is a palindrome")
#         else:
#             print(f"{n} is not a palindrome")
#
# a = input("Enter a number: ")
# number = Palindrome()
# number.palindrome(a)