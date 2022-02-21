import random

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tSquid game\t\t\t\t\t\t\t\t\t\t\t\t")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t You Loss You Die")
tot_me = 10
tot_com = 10
for i in range(0, 5):
    print("Enter your choice")
    you = input("Enter o for odd and e for even\n")
    youi = int(input("Enter your pebbles you want to risk\n"))
    com = random.randint(1, 10)
    if youi > tot_me:
        print("You do not have this much pebbles\n Try lesser number")
        continue
    if com > tot_com:
        print("Computer do not have this much pebbles\n Try lesser number")
        continue
    print(f"Computer risked {com} pebbles\n")
    if you == 'o' and com % 2 == 1:
        print(f"You got {com} number of pebbles")
        tot_me = tot_me + com
        tot_com = tot_com - com
        print(f"Now you have {tot_me} pebbles left\nComputer have {tot_com} pebbles left\n")
        if tot_me == 0:
            print("Computer is the winner of The Squid Game\n you are dead")
            break
        if tot_com == 0:
            print("You are the winner of The Squid Game\n Computer you are dead")
            break

    elif you == 'e' and com % 2 == 0:
        print(f"You got {com} number of pebbles")
        tot_me = tot_me + com
        tot_com = tot_com - com
        print(f"Now you have {tot_me} pebbles left\nComputer have {tot_com} pebbles left\n")
        if tot_me == 0:
            print("Computer is the winner of The Squid Game\n you are dead")
            break
        if tot_com == 0:
            print("You are the winner of The Squid Game\n Computer you are dead")
            break

    elif you == 'o' and com % 2 == 0:
        print(f"Computer got {youi} number of pebbles")
        tot_me = tot_me - youi
        tot_com = tot_com + youi
        print(f"Now you have {tot_me} pebbles left\nComputer have {tot_com} pebbles left\n")
        if tot_me == 0:
            print("Computer is the winner of The Squid Game\n you are dead")
            break
        if tot_com == 0:
            print("You are the winner of The Squid Game\n Computer you are dead")
            break

    elif you == 'e' and com % 2 == 1:
        print(f"Computer got {youi} number of pebbles")
        tot_me = tot_me - youi
        tot_com = tot_com + youi
        print(f"Now you have {tot_me} pebbles left\nComputer have {tot_com} pebbles left\n")
        if tot_me == 0:
            print("Computer is the winner of The Squid Game\n you are dead")
            break
        if tot_com == 0:
            print("You are the winner of The Squid Game\n Computer you are dead")
            break

    else:
        print("Please enter the correct input")

if tot_me > tot_com:
    print("You are the winner of The Squid Game\n Computer you are dead")
elif tot_me == tot_com:
    print("It's A Tie")
else:
    print("Computer is the winner of The Squid Game\n you are dead")
