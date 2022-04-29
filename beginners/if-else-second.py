# moonwalking

age = int(input("What is your age?"))
bill = 0

if age >= 8:
    print("You're eligible for moon walking.")    
    if age <= 12:
        bill = 2
        print(f"You can moonwalk with your friends. Your bill is {bill}")
    elif age <= 18:
        bill = 4
        print(f"You can moon walk alone. Your bill is {bill}")
    else:
        bill = 6
        print(f"You're adult. Your bill is {bill}")
    souvenir = input("Want a souvenir from moon? Answer y or n")
    
    if souvenir == "y":
        bill = bill + 3
                
    print(f"Your total bill is {bill}")
else:
    print("You're not eligible for moon walking.")


'''
You're eligible for moon walking.
You're adult. Your bill is 6
Your total bill is 9
'''