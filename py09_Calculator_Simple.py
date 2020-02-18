print("Welcome to Calculator.py")
print("")

loop = 1
choice = 0
print('Select any Option from below:-')
print("")
print('Option 1: Add')
print('Option 2: Subtract')
print('Option 3: Multiply')
print('Option 4: Divide')
print('Option 5: Quit Program')
print("")

choice = int(input('Enter Option: '))

while loop == 1:

    if choice == 1:
        print('Addition')
        total = int(input("First Number: ")) + int(input("Second Number: "))
        print("Total: " + str(total))
        print("")
        
    elif choice == 2:
        print('Subtraction')
        total = int(input("First Number: ")) - int(input("Second Number: "))
        print("Total: " + str(total))
        print("")

    elif choice == 3:
        print('Multiplication')
        total = int(input("First Number: ")) * int(input("Second Number: "))
        print("Total: " + str(total))
        print("")

    elif choice == 4:
        print('Division')
        total = int(input("First Number: ")) / int(input("Second Number: "))
        print("Total: " + str(total))
        print("")
        
   elif choice == 5:
        loop = 0
        print('Quiting Program. Thankyou for using Calculator.py')

