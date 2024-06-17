     #THIS PROGRAM IS FOR AIRTEL TALK-TIME CREDIT
print("WELCOME BACK\n");
dial = str(input(("Dial *118# to Access the Service\n")));
if dial == "*118#":
    myMenu = int(input(("Reply with:\n\n1 for Siliza Airtime\n2 for Eligibility Check\n3 for Payment\n4 for Help\n5 for Balance Check\n")));
        #for option 1
    if myMenu == 1:
         print("Dear Customer, your request was unsuccessful.\nTop up more to qualify for this service.");

        #for option 2
    elif myMenu == 2:
        print("Dear Customer, your request was unsuccessful.\nTop up more to qualify for this service.");

        #for option 3
    elif myMenu == 3:
        print("Please recharge with K0.0000\nto fully payback your loan.");

        #for option 4
    elif myMenu == 4:
        select = input(("Reply With:\n\n1 Qualification\n2 Repayment\n# Main Menu\n"));
            #option 4 sub 1
        if select == "1":
            print("To qualify you must have been an active Aitel subscribe for atleast 1 month.\nReply with:\n\n1 to return");
            replyReturn = int(input());

                #option 4 sub 2 of sub 1
            print(select);
        
            #option 4 sub 2
        elif select == "2":
            print("The advanced amount should be paid back within 48hrs.\nTo repay, please recharge your line.")
            
            #option 4 sub 3
        elif select == "#":
            print(myMenu);
    
            #if option  not there
        else:
            print("Not true");

        #for option 5
    elif myMenu == 5:
        print("Dear Customer, your request is being processed.\nYou will receive an SMS confirmation shortly.");

        #for input not true
    else:
        print("input invalide");

else:
    print("Invalide MMI Code"); 