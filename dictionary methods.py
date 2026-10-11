#Returns all key
dict = {
    "English" : 50,
    "physics": 50,
    "Maths" :50
}
print(dict.keys())

#Return all values

print(dict.values())

#return all key and values pairs as tuples

print(dict.items())

#Return the key according to values 

print(dict.get("English"))

#insert the specific item in dictionary

dict.update({"mango":"fruit"})
print(dict)