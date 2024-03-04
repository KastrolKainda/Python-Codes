    ##THIS PROGRAM RUNS ZAMTEL SERVICE
print("To Acces This Service. Please DIAL *117#");
dial = input();

    #if *117# is true: SHOW THIS!!
if dial=="*117#":
    print("The Best Offers In Town:");
    print("1) Vibez\n2) SupaCheza\n3) Ni Yathu\n4) Freedom\n5) Data Offers\n6) Balance\n7) Green Thursday\n8) Velocity Lite\n9) Buy 4 Other");
    select = int(input());
        ## for case 1>>>
    if select==1:
        print();
    
        ## for case 2>>>
    elif select==2:
        print();
    
        ## case 3>>>
    elif select==3:
        print();
    
        ## case 4>>>
    elif select==4:
        print();
    
        ## case 5>>>
    elif select==5:
        print();
    
        ## for case 6>>>
    elif select==6:
        print();    
    
        ## for case 7>>>
    elif select==7:
        print();    
    
        ## for case 8>>>
    elif select==8:
        print();    
    
        ## for case 9>>>
    elif select==9:
        print();  
    
        ## for invalide option
    else:
        print("Check the option entered");

    #if *117# ISN'T TRUE
else:
    print("Invalid MMI code\n\n");


