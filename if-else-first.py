# moonwalking

age = int(input("What is your age?"))

if age >= 8:
    print("You're eligible for moon walking.")    
    if age <= 12:
        print("You're eligible for moon walking with your friends.")
    elif age <= 18:
        print("You're eligible for moon walking alone.")
    else:
        print("You're eligible for moon walking with your lover.")
else:
    print("You're not eligible for moon walking.")