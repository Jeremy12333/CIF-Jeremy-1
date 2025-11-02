from random import randint
low=int(input("input the lowest number for a number range "))
high=int(input("input the highest number for a number range"))
randomnum= randint(low,high)
answer= "yes"
while answer=="yes":
    guess=int(input("guess the number from the range"))
    if guess== randomnum:
        print("you guessed correctly!")
        break
    else:
        if guess > randomnum:
            print ("you failed, you guessed too high")
            answer=str(input("do you wanna try again?(yes or no)"))
        else:
            print("You failed, your guess was too low")
            answer=str(input("do you wanna try again?(yes or no)"))
print("Thank you for playing!")



