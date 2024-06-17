        #THIS PROGRAM CALCULATES THE BODY MASS INDEX (BMI) CALCULATOR

print("WELCOME BACK\nThis Program Is For Body Mass Index (BMI)\n");
        #for weight
bodyWeight = float(input(("Enter your Weight(kg)\n")));
        #for height
bodyHeight = float(input(("Enter your Height(cm)\n")));

        #formula for BMI
BMI =  float (bodyWeight) / float(bodyHeight * bodyHeight);

        #parameters for botdweight and body height should not be equal to 0
if(bodyHeight >= 0.1 and bodyWeight >= 0.1):
                #if BMI is less than 18KGs
        if BMI <= 17.9:
            print("Your Body Mass Index(BMI) = ",BMI,"\nYou are Underweight");
        
                #if BMI is between 18KGs to 24KGs
        elif BMI >= 18.0 and BMI <= 23.9:
            print("Your Body Mass Index(BMI) = ",BMI,"\nYou are Average");
        
                 #if BMI is between 18KGs to 24KGs
        elif BMI >= 24.0 and BMI <= 34.9:
            print("Your Body Mass Index(BMI) = ",BMI,"\nYou are Normal");
        
                #if BMI is between 18KGs to 24KGs
        elif BMI >= 35.0 and BMI <= 49.9:
            print("Your Body Mass Index(BMI) = ",BMI,"\nYou are Obessity");
        
                 #if BMI is more than 50KGs
        else:
            print("Your Body Mass Index(BMI) = ",BMI,"\nYou are Overweight");


        #If both weight and height is less than zero (0)
else:
    print("ERROR\nWeight and Height cannot be less or equal to 0!!");