    #THIS IS FOR SIMPLE VOTING PROGRAM
print("\nTo Vote Please Enter Your Age\n");
print("Enter Your Age\t");
age = int(input());

    #if age is greater or equal to 18, show this
if age >=18:
    print("You are eligible to vote\n");

    press = int(input("Press 10 to continue\n"));

        #if 10 has been entered show this on screen
    if press==10: 
        print("Please Select:\n1. For Presidential\n2. For Vice President\n3. For Ministers");
        sel = int(input());
        if sel==1:
            print("Thank You for Choosing this oprtion!!");

        elif sel==2:
            print("Thank you for selecting this part!!");

        elif sel==3:
            print("This is a greate choice you have decided!!");

        else:
            print("That's Not True!\n");

        #if 10 is not entered 
    else:
        print("That figure Doesn't Exist!!\n");  
     
    #if age is less than 18: show this
else:
    print("Sorry! You can't vote.\n\n");