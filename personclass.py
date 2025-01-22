class Student():
    def __init__ (self,name,age,gender,school,city):
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school
        self.city = city
    def display(self):
        print("details of the student")
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.school)
        print(self.city)  
    def change_details(self):
     self.name = input("new name")   
     self.age = input("new age")  
     self.gender = input("new gender")  
     self.school = input("new school")  
     self.city = input("new city")  
Tim = Student("Tim",16,"Boy","Midtown High","New York") 
Tim.display()
Tim.change_details()
Jane = Student("Jane",16,"Girl","Midtown High","New York")
Jane.display()
Jane.change_details()
