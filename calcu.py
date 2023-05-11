
print("|||||||||||______________||||||||")
print("---------This is the Beginning-------")
print("__________Let Start something awesome")
print(" I can do ADDITION SUBTRACTION, MULTIPLICATION, DIVISION, MEAN, RANGE")

#user input
Enter_value1 = input("Enter Your First Value Here: ")
Enter_sign   = input("Enter SIGN : ")
Enter_value2 = input("Enter Your Second Value Here:")

calc1 = float (Enter_value1)
calc2 = float(Enter_value2)
if Enter_sign == '-':
    subtract = calc1 - calc2
    print('You are subtracting' )
    print(calc1)
    print('From')
    print(calc2)
    print('and answer is')
    print(subtract)
elif Enter_sign =='+':
    addition = calc1 + calc2
    print('You are adding' )
    print(calc1)
    print('TO')
    print(calc2)
    print('and answer is')
    print(addition)
elif Enter_sign == '/':
    dividing = calc1 / calc2
    print('You are dividing' )
    print(calc1)
    print('By')
    print(calc2)
    print('and answer is')
    print(dividing)
elif Enter_sign == '*':
    multplication = calc1*calc2
    print('You are Multiplying' )
    print(calc1)
    print('By')
    print(calc2)
    print('and answer is')
    print(multplication)



    
    





