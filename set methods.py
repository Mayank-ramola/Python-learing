#adds an elements
collections = {2,6,8,8}
collections.add(3)
print(collections)

#remove an elements

collections.remove(8)
print(collections)

#empties the set

collections.clear()
print(collections)

#pops a random value
collections2 = {"hello", "kite", 2 ,"many",28,6}
print(collections2.pop())

#combine both set values and return new
collections2 = {"hello", "kite", 2 ,"many",28,6}
print(collections.union(collections2))

#combines commons values and returns new

collections = {2,6,8,8}
ollections2 = {"hello", "kite", 2 ,"many",28,6}
print(collections.intersection(collections2))