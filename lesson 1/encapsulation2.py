class circle:
    def __init__(self):
        self.__side= 10
    def area(self):
        print("side is:",self.__side)
        print("my area is:",self.__side*2)

ob =circle()
ob.__side=15
ob.area()
