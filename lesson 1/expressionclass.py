class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("The addition of the three numbers is:", result)

obj1 = Expression(5, 10, 15)
obj1.add_numbers()

obj2 = Expression(3, 7, 11)
obj2.add_numbers()

obj3 = Expression(9, 6, 5)
obj3.add_numbers()
