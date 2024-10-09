import random

Fruits = ["Apple","Orange","Banana"]
print(Fruits)
print(Fruits[1])
print(Fruits[2])

Fruits.append("Cherry")  
print(Fruits)

Fruits.remove("Apple")
print(Fruits)
if "Apple" in Fruits:
    print("Apple is Present")

else:
    print("Apple is not Present")  

if "Peach" in Fruits:
    print("Peach is Present")

else:
    print("Peach is not Present")         
    Fruits.append("Peach")
    print(Fruits)    
#
for fruit in Fruits: 
    print(fruit)