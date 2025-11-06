print ("Hello World!")
print ("Hello", "World")
print (13 + 59)
print (20/5)
print (6*12)
print (100%5)
print (100 ** 2)
print (12 + 4, 10/2, 3*12, 180%20, 30 ** 4)
print ("Exponent=", 12**2, "Remainder=", 40%5, "Product=", 5*9, "Quotient=",10/2, "Sum=",55 + 5)

age = 29 
print ("My age=", age)
older = age+5
print ("My brother's age", older)
print ("My sister's age", age -4)
var1=age+older
print ("Age", var1)
var2=age/older
print (var2)
var3=age-older
print (var3)
print (f"Hello {age + 7} !")

name = "Lhaiza"
print(f"Hello {name}!")
print (f"{name} likes to bake cookies.")

w = str(input("Enter name"))
e = float(input("Enter age")) 
r = str(input("Enter University"))
y = str(input("Course")) 
t = float(input("Enter Year"))

m = float(input("Enter Biology mark"))
n = float(input("Enter Chemistry mark"))
b = float(input("Enter Physics mark"))
v = float(input("Enter Math mark"))
c = float(input("Enter English mark"))
average = ((m+n+b+v+c)/5)
print (f"Your average is : {average}")
percentage = average%200
print (f"Your percentage is : {percentage}%")

#simple conditional statement
marks = int(input("Enter your marks:"))
if marks>100 and marks>=70:
    print("Valid Marks")
elif marks>=70:
    print("You have passed!")
elif marks<=70:
    print("You have failed")
else:
    print ("Invalid marks")

#ask the 100-80 A 
marks = int(input("Enter Marks:"))
if marks >=100 or marks<0:
    print("Invalid Marks")
elif marks >=80:
    print("B")
elif marks <80 and marks >=70:
    print("C")
elif marks >70 and marks >=60:
    print("D")
else:
    print("You failed")


