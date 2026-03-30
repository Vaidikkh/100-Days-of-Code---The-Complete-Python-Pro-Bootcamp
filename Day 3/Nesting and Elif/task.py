print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age>=18:
        print("the amound you have to pay is $12")
    else:
        print("the amound you have to pay is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
