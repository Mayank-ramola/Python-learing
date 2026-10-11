#WAP to enter marks od 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value

phy = int(input("Enter marks of physics: "))
chem = int(input("Enetr marks of chem: "))
maths = int(input("Enter marks of maths: "))

dict = {
    "phy": phy,
    "chem": chem,
    "maths": maths
}
print(dict)