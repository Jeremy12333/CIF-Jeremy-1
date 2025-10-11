from random import randint 
random_num= randint(0,20)
number=int(input("pick a number from 0-20 \n"))
if number == random_num:
    print("you guessed right")
else:
    print("you failed")
