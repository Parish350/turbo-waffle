import random

usernames = ["Shaker","Jumpy","Dancy","Cooly"]
print(usernames)
name = input("Enter your username")

if name in usernames:
    print("name is present")
else:
    print("name is not present")

usernames.append("Cooly")  
print(usernames)

usernames.remove("Shaker")
print(usernames)
if "Shaker" in usernames:
    print("Shaker is Present")

else:
    print("Shaker is not Present")  

if "Droopy" in usernames:
    print("Droopy is Present")

else:
    print("Droopy is not Present")         
    usernames.append("Droopy")
    print(usernames)    
#
for usernames in usernames: 
    print(usernames)