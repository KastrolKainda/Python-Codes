        #THIS PROGRAM  IS FOR AIRTEL IKALI DATA BUNDLE#

print("\nTo Acces This Service. Please DIAL *117#");
dial = input();

    #if *117# is true: SHOW THIS!!
if dial=="*117#":
    print("Airtel 100% 4G");
    print("1.Ikali - Data and Voice\n2.Airtel SoChe Pack\n3.All networks SoChe\n4.Data Packs\n5.Buy for Other\n6.Balance Check\n7.Night Data\n8.Siliza - Airtime Loan\nn Next");
    sel = int(input());

        #CASE 1-->
    if sel==1:
        print("Select\n1.K2=12 Airtel Min,24Hrs\n2.K2=12 All Networks Min,24Hrs\n3.K5=35 Airtel Min,7Day\n4.K2=150MB,24Hrs\n5.K10=2GB,7Day\n6.K5=400MB,7Day");
        a = int(input());
                #FOR CASE 1, OPTION 1>>
        if a==1:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 1>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you\nwill receive a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");
        


            #FOR CASE 1, OPTION 2>>
        elif a==2:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 2>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you will receice a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");



            #FOR CASE 1, OPTION 3>>
        elif a==3:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 3>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you will receice a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");



            #FOR CASE 1, OPTION 4>> 
        elif a==4:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 4>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you will receice a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");



            #FOR CASE 1, OPTION 5>>
        elif a==5:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 5>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you will receice a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");


            #FOR CASE 1, OPTION 6>>
        elif a==6:
            print("1. Main Account\n2. Airtel Money");
            a1 = int(input());

                        #FOR CASE 1, OPTION 6>> PAYMENT OPTION        
            if a1==1: #FOR MAIN ACCOUNT
                print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best\ntransaction experience use My Airtel App");
                print("1) Download The App \n");

            elif a1==2: #FOR AIRTEL MOBILE MONEY
                print("Enter PIN")
                a12 = int(input());
                print("Thank you for confirming your PIN. Your transaction is being processed and you will receice a confirmation SMS soon.\n")

            else:  #FOR UNKNOWN OPTION
                print("Recheck The Options!!\n");

            #FOR UNKNOWN INVALID OPTION
        else:
            print("That option doesn't exist");




        #CASE 2-->
    elif sel==2:
        print("");

        #CASE 3-->
    elif sel==3:
        print("");

        #CASE 4-->
    elif sel==4:
        print("");

        #CASE 5-->
    elif sel==5:
        print("");

        #CASE 6-->
    elif sel==6:
        print("");

        #CASE 7-->
    elif sel==7:
        print("");

        #CASE 8-->
    elif sel==8:
        print("");

        #CASE 0: FOR INVALID CASE SELECTED-->
    else:
        print("That option isn't there!!\n");   

    #if *117# is not TRUE
else:
    print("Invalid MMI code\n");
