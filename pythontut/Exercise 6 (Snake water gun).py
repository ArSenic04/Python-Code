import random
lis=["s","w","g"]
chance=5
no_c=0
you_p=0
cmp_p=0
print("\t \t Snake,Water,Gun\n\n")
print("s for Snake\nw for Water\ng for Gun")
while no_c < chance:
    y = input("Enter your choice")
    ran = random.choice(lis)
    if y == ran:
        print("Tie you Both got 0 points")
    elif y == 's' and ran == 'g':
        cmp_p=cmp_p+1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("Computer got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    elif(y=='g' and ran=='w'):
        cmp_p = cmp_p + 1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("Computer got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    elif(y=='g' and ran=='s'):
        you_p=you_p+1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("You got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    elif(y=='s' and ran=='w'):
        you_p = you_p + 1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("You got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    elif(y=='w' and ran=='s'):
        cmp_p = cmp_p + 1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("Computer got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    elif(y=='w' and ran=='g'):
        you_p = you_p + 1
        print(f"Your guess {y} and computer guess {ran}\n")
        print("You got 1 point")
        print(f"Your point is {you_p} and computer point is {cmp_p}\n")
    else:
        print("Please correct your input")
    no_c=no_c+1
    print(f"{chance-no_c} is left out of {chance}\n")
print("Game Over")
if(cmp_p==you_p):
    print("Tie")
elif(cmp_p>you_p):
    print(f"Computer won by {cmp_p-you_p}")
else:
    print(f"You won by {you_p-cmp_p}")