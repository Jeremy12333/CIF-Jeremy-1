
print("Tech Store")
print("Welcome to the store!\nHere's what we sell:")
items=["1 Laptops", "2 Mice", "3 Cables", "4 Phones", "5 Watches"]
price=["2000", "20", "15", "1000", "400"]
count=0
for item in items:
    print(item , "$", price[count])
    count= count +1 
answer = "yes"
total= 0
while answer =="yes":
    print("What would you like to buy?\n ")
    code=int(input("enter the code of the item\n"))
    print(items[code - 1], "$", price[code-1])
    many=int(input("how many would you like\n"))
    notwholetotal=int(price[code-1]) * many 
    total=notwholetotal + total
    answer = input("do you want to continue shopping?\n")
membership= input (" do you have a membership? \n ")
if membership == ("yes") :
    total = total * 0.80 
    print ("thank you for supporting, 20 %  discount for you \n")
else :
    print ("no discount for you hahahaha")
print ("your total is" ,total) 


