    #FOR FUN AND TESTING ONLY
print("Welcome Back\n\nWhich type of Garget do you want?");
choice = int(input(("1 Phone\n2 Tablet\n3 Laptop\n4 Desktop\n")));

match choice:
            #for case or option 1 >> for PHONES
    case 1:
        print("For Phones\nPress:\n1. Samsung\n2. iPhone\n3. Windows");
        phonePress = int(input());
                #case >> option 1
        match phonePress:
            case 1:
                print("You selected Samsung Phone");
                 #case >> option 2
            case 2:
                print("You selected iPhone Phone");
                 #case >> option 3
            case 3:
                print("You selected Windows Phone");
    
                #case >> option 1 invalid
            case _:
                print("Not there");
    

            #for case or option 2 >> for TABLETS
    case 2:
        print("For Tablets\nPress:\n1. Microsoft\n2. Google");
        tabletPress = int(input());
             #case >> option 1
        match tabletPress:
            case 1:
                print("You selected Microsoft Tablet");
                 #case >> option 2
            case 2:
                print("You selected Google Tablet");

                #case >> option 1 invalid
            case _:
                print("Not there");


            #for case or option 3 >> for LAPTOPS
    case 3:
        print("For Laptops\nPress\n1. Dell\n2. HP\n3. Lenova");
        laptopPress = int(input());
            #case >> option 1
        match laptopPress:
            case 1:
                print("You selected Dell Laptop");
                 #case >> option 2
            case 2:
                print("You selected HP Laptop");
                 #case >> option 3
            case 3:
                print("You selected Lenova Laptop");
    
                #case >> option 1 invalid
            case _:
                print("Not there");
    

            #for case or option 4 >> for DESKTOPS
    case 4:
        print("For Desktops\nPress:\n1. Dell\n2. HP\n3. Lenova");
        desktopPress = int(input());
            #case >> option 1
        match desktopPress:
            case 1:
                print("You selected Dell Desktop");
                 #case >> option 2
            case 2:
                print("You selected HP Desktop");
                 #case >> option 3
            case 3:
                print("You selected Lenova Desktop");
    
                #case >> option 1 invalid
            case _:
                print("Not there");

            #for default value
    case _:
        print("Invalid input");