class Grandfather:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
    

  def printname(self):
    print(self.firstname, self.lastname)

class Grandson(Grandfather):
  def __init__(self, fname, lname,age):
    super().__init__(fname, lname)
    self.age = age

x = Grandson("Chandler","bing",24)
x.printname()
print(x.age)