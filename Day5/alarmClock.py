from time import sleep
if __name__=="__main__":
    print("1. set Alarm\n 2. exit")
    choice=int(input("Enter your choice:\n"))
    if choice==1:
        mins=int(input("Alarm time: Enter minutes remaining from current time:"))
        if mins<0:
            print("Enter future time .. It can't be negative")
        elif mins==0:
            print("Alarm Started..!   WAKE UP..!!!!")
        elif mins==1:
            print("sleep for 1 minute")
            sleep(1*60)
            print("Alarm Started..!   WAKE UP..!!!!")
        else:
            print("sleep for {} minutes".format(mins))
            sleep(mins * 60)
            print("Alarm Started..!   WAKE UP..!!!!")
    else:
        exit(0)