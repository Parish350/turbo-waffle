class Car():
    def __init__ (self,name,colour,vehicletype,model):
        self.name = name
        self.colour = colour
        self.vehicletype = vehicletype
        self.model = model
    def display(self):
        print("details of the car")
        print(self.name)
        print(self.colour)
        print(self.vehicletype)
        print(self.model)
    def change_details(self):
     self.name = input("new name")   
     self.colour = input("new colour")  
     self.vehicletype = input("new vehicletype")  
     self.model = input("new model")   
Tesla = Car("Tesla","White","Electric","Model 3") 
Tesla.display()
Tesla.change_details()    
Audi = Car("Audi","White","Diesel","A4") 
Audi.display()
Audi.change_details()
