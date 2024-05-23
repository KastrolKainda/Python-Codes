    #THIS PROGRAM IS FOR SIMPLE CALCULATOR

print("WELCOME BACK!");
            #first number
FNumber= input("Enter the first number\n");
            #second number
SNumber = input("Enter the second number\n");
         #options on the calculator
print("Select:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division");
select = int(input());
if select == 1:
    sum = int(FNumber) + int(SNumber); #addition (+)
    print("The sum of two numbers = ",sum); #addition

elif select == 2:
    sub = int(FNumber) - int(SNumber); #subtraction (-)
    print("The substraction of two numbers = ",sub); #subtraction

elif select == 3:
    mul = int(FNumber) * int(SNumber); #multiplication (*)
    print("The multiplication of two numbers = ",mul);  #multiplication

elif select == 4:
    div = int(FNumber) / int(SNumber); #divition (/)
    print("The division of two numbers = ",div);    #division

else:
    print("Invalid input");   #not on the list