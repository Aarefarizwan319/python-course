class student:
        grade = 10
        name ="pluto"
        def introduction(self):
                print("hi  i am a student")
        def details(self):
                print("my name is:",self.name)
                print("i am in grade :",self.grade)
ob = student()
ob.introduction()
ob.details()
