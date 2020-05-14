import random
val=0
print("Game Rule:\n Autoplayer select a number between 1 to 9\n You will get 3 chance to guess the number if you guess correctly you will win 5$ else you loose 3$")
while True:
    print("1. Play Game")
    print("2. exit Game")
    choice = int(input("Enter your choie: \n"))
    if choice==1:
        selected=random.randint(1,9)
        # print(selected)
        num=int(input("guess the number\n"))
        if num==selected:
            print("You won.!!")
            val=val+5;
        else:
            num = int(input("wrong..!! guess the number again\n"))
            if num == selected:
                print("You won.!!")
                val = val + 5
            else:
                num = int(input("wrong..!! guess the number again\n"))
                if num == selected:
                    print("You won1.!!")
                    val = val + 5
                else:
                    val=val-3
                    print("You Loose")
    elif choice==2:
        if val>=0:
            print("You have won a total of {}$".format(val))
        else:
            print("You lost a total of {}$".format(abs(val)))
        break
    else:
        print("Invalid choice. Try again")
