        #BASIC INPUT OF THE SYSTEM
print("WELCOME BACK");
myName = input(("Enter your Full Names\n"));

print("Hello", myName);
        #IF CHOICES ARE TRUE
enterValue = input(("To Continue. Please enter 10\n"));
if enterValue == "10":
    select = input(("1. Apply\n2. Become a Member\n3. Register\n4. Get in Touch\n00 Cancel\n"));
            
            # for application or enrollment form
    if select == "1":
        print("To Apply\nFill in the Application Form");
        fullname = input(("Enter your Full Names\n"));
        phone = int(input(("Enter your Phone Number\n")));
        address = input(("Enter your Phyical Address\n"));
        email = input(("Enter your Email Address\n"));
        print("Thank You for providing your\nDetails and we will get back to you soon.");
    
            # for membership form
    elif select == "2":
        print("To Become a Member\nFill in the Membership Form");
        fname = input(("Enter your First Name\n"));
        lname = input(("Enter your Last Name\n"));
        phone = int(input(("Enter your Phone Number\n")));
        address = input(("Enter your Phyical Address\n"));
        email = input(("Enter your Email Address\n"));
        print("Thank You for providing your\nDetails and we will get back to you soon.");
    
            # for registration form
    elif select == "3":
        print("To Register\nFill in the Registration Form");
        fullname = input(("Enter your Full Names\n"));
        nrc = input(("Enter your NRC/Passport Number\n"));
        phone = int(input(("Enter your Phone Number\n")));
        address = input(("Enter your Phyical Address\n"));
        email = input(("Enter your Email Address\n"));
        birth = input(("Enter your Date of Birth\n"));
        print("Thank You for providing your\nDetails and we will get back to you soon.");
    
    elif select == "4":
        print("To get in Touch. Click here www.my-site.com");
    
    elif select == "00":
        print("Program Cancelled");
    
    else:
        print("Check the available options and try again");

        #FOR INVALID CHOICES
else:
    print("Invalid input");
