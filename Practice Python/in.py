Points = int(input("Enter your Points:"))
while Points <0 or Points >100:
    print("Invalid Score")
Points = int(input("Enter your Points:"))
if Points >= 50:
    print("You passed! Go to the next round!")
else:
    print("You failed, Try again!")




guest= ["Luffy", "Nami", "Zoro","Sanji","Usopp","Chopper","Robin","Franky","Brook","Jinbe"]
print (f"You are invited {guest[0]} to my party!")
print (f"You are invited {guest[1]} to my party!")
print (f"You are invited {guest[2]} to my party!")
print (f"You are invited {guest[3]} to my party!")
print (f"You are invited {guest[4]} to my party")
print (f"You are invited {guest[5]} to my party!")               
print (f"You are invited {guest[6]} to my party!")
print (f"You are invited {guest[7]} to my party!")
print (f"You are invited {guest[8]} to my party!")  
print (f"You are invited {guest[9]} to my party!") 
   

names= ["Luffy", "Nami", "Zoro","Sanji","Usopp","Chopper","Robin","Franky","Brook","Jinbe"]
print (names)
names [2]="Yamato" #replace the value
print(names)
names.append("Vivi") # adds value
print (names)
names.insert(1,"Ace") #inserts value
print (names)
del(names[2]) 
print(names)
names.remove("Usopp") #removes value
print (names)
names.sort() #sort alphabetically
print(names)
names.reverse() #reverse the order
print(names)

#slicing
names1= ["Luffy", "Nami", "Zoro","Sanji","Usopp","Chopper","Robin","Franky","Brook","Jinbe"]
print(names1[:5])
print(names1[3],names1[2],names1[0])

countries= ["Pakistan", "India", "Japan", "Iran", "Iraq", "Palestine", "Sudan"]
print (countries)
countries.sort()
print (countries)
countries1= ["Pakistan", "India", "Japan", "Iran", "Iraq", "Palestine", "Sudan"]
countries1.reverse()
print(countries1)
countries.reverse()
print(countries)
countries.append("Russia","China")
countries.remove("Japan")
print (countries)




    





    

