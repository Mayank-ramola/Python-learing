#Write a recursive function to print all elements in a list 

# list = ["Mango", "orange", "grapes", 23,50]
# def ele(list):
#     if (list != list):
#         return 0
#     else:
#         return list
    

def print_list(list , idx=0):
    if(idx == len(list)):
        return
        
    print(list[idx])
    print_list(list, idx+1)


num = [3,5,3,5,348,6,56]
print_list(num)    