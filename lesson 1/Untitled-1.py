class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog my name is {self.name} i am {self.age} years old.")
    def sound(self):
        print("bark")
        
class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat my name is {self.name} i am {self.age} years old.")
    def sound(self):
        print("meow")
        
cat1=cat("zorrow",3)
dog1=dog("bozo",4)

for animal in (cat1,dog1):
    animal.info()
    animal.sound()
    