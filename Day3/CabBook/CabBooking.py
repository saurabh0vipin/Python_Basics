vehicles =	{
  "Swift ": 45,
  "Maruti": 30,
  "Vagnor": 30,
  "innova": 40,
  "safari": 45
}

class bookCab():
    def __init__(self):
        ## name and speed assignment
        print("vehicle name\t\tspeed")
        print("________________________________")
        count=1;
        for x in vehicles:
            print(str(count)+". "+x+"\t\t"+str(vehicles[x])+"\n")
            count=count+1;
        print("Choose vehicle from available list\n")
        
        choice=int(input("Enter your choice no here:(between 1-5) \n"))
        if choice==1:
            self.CarName="Swift "
            self.speed=vehicles["Swift "]
        elif choice==2:
            self.CarName="Maruti"
            self.speed=vehicles["Maruti"]
        elif choice==3:
            self.CarName="Vagnor"
            self.speed=vehicles["Vagnor"]
        elif choice==4:
            self.CarName="innova"
            self.speed=vehicles["innova"]  
        else:
            self.CarName="safari"
            self.speed=vehicles["safari"]
            
        ##Seat and distance
        self.seats=int(input("Enter the number of seats you wanna book:\n"))
        location=[input("Enter pickup location\n"),input("Enter drop location\n")]
        self.distance=abs(ord(location[0][0])-ord(location[1][0]))*10
    
    def getTotalFare(self):
        return self.seats*(12*self.distance)
def main():            
    user=bookCab()
    print("Distance between pickup and drop point is: {}km".format(user.distance))
    print("Total payble amount is : ${}".format(user.getTotalFare()))
    
main()

