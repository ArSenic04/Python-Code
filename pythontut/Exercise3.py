"""Game of Gussess """
import random
print("Enter the number")
num=int(input())
guess=0
my=random.randint(1,100)
while (num!=my):
    if num>my:
        print("Lower Number please")
        guess=guess+1
        print("Enter the number again")
        num = int(input())
    elif num<my:
        print("Higher number please")
        guess = guess + 1
        print("Enter the number again")
        num = int(input())
    else:
        print("You Gussed my number")
        guess = guess + 1
        break

print("You guessed in",guess+1,"chance")
