#create a class called order which stores item and its price.
#use dunder function __gt__() to convey that:
# order1 >order2 if price of order1 > price of order2



class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price 
    def __gt__(self, odd2):
        return self.price > odd2.price
    
odd1 = Order("orange", 100)   
odd2 = Order("mango", 200)       

print(odd1>odd2)