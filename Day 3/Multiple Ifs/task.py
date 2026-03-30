print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 12
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("do you want to take a photo if yes then y else n for no ")
    if wants_photo =="y":
        print("the total is ",bill + 3 )
    else :
        print("enjoy")
else:
    print("Sorry you have to grow taller before you can ride.")
