def display_message():
    print("I have no money")
display_message()

def display_message():
    """Display a message about what I'm learning."""
    msg= "I've learnt how to store messages using functions."
    print(msg)
display_message() 

def favorite_book(title):
    """Display a message aboout someone's favorite book."""
    print(title + " is one of my favorite book.")

favorite_book("Lonely castle in the mirror")

#Write a code where you create a function to display the size 
# of the shirt along with the message to be printed on it. 
# Give appropriate ame to the function.

def shirt_size(size):
    """ONE PIECE"""
    print(size + """ ONE PIECE""")

shirt_size("Small size:")
shirt_size("Medium size:")
shirt_size("Large size:" )

def shirt_customize(message,size):
    
    print (" The message on my Shirt is" + message)
    print(" The size of my shirt is" + size)

shirt_customize (" Pirate"," XL")

information= {
    "first_name" : "Erryl",
    "Second name" : "Lhaiza",
    "age": "18",
    "hometown": "Sharjah"
}

print (information)
print (information["first_name"])
information ["age"] = "18"
print(information)

del information ["age"]
print (information)

x = information.get ("hometown")
print (x)

information.pop("Second name")
print (information)

information.update ({"age":"19"})
print (information)

information.clear()
print (information)

print (information.keys())
print (information.values())









