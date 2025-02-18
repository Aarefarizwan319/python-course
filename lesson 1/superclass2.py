class Grandfather:
  def __init__(self,fname,lname,age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname,self.age)

class Grandson(Grandfather):
  def __init__(self, fname, lname,age):
    super().__init__(fname, lname)
    self.age = age

x = Grandson("Chandler","bing",24)
x.printname()
print(x.age)