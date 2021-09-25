playagain="y"
while playagain=="y" or "Y":
    print("Welcome to the Flarsheim Guesser!")
    print("Please think of a number between and inlcuding 1-100")
    remainder3=int(input("What is the remainder when your number is divided by 3?"))
    while remainder3<0 or remainder3>=3:
        if remainder3>=3:
            print("The value entered must be less than 3")
            remainder3=int(input("What is the remainder when your number is divided by 3?"))
        elif remainder3<0:
            print("The value enter must be 0 or greater")
            remainder3=int(input("What is the remainder when your number is divided? by 3?"))

    remainder5=int(input("What is the remainder when your number is divided by 5?"))
    while remainder5<0 or remainder5>=5:
        if remainder5>=5:
            print("The value entered must be less than 5")
            remainder5=int(input("What is the remainder when your number is divided by 5?"))
        elif remainder5<0:
            print("The value entered must be 0 or greater")
            remainder5=int(input("What is the remainder when your number is divided by 3?"))

    remainder7=int(input("What is the remainder when your number is divided by 7?"))
    while remainder7<0 or remainder7>=7:
        if remainder7>=7:
            print("The value entered must be less than 7")
            remainder7=int(input("What is the remainder when your number is divided by 7?"))
        elif remainder7<0:
            print("The value entered must be 0 or greater")
            remainder7=int(input("What is the remainder when you number is divided by 7?"))

    def secretnum(remainder3,remainder5,remainder7):
        for i in range(1,101):
            if i%3==remainder3 and i%5==remainder5 and i%7==remainder7:
                return i
    number=secretnum(remainder3,remainder5,remainder7)
    print("Your number was",number)
    print("How amazing is that?")
    while(True):
        replay=input("Do you want to play again? Y to continue, N to quit ==>")
        if (replay=="Y" or replay=="y" or replay=="N" or replay=="n"):
            break;
        if replay=="n" or replay=="N":
            break
        print()