print('Enter your age: ')

your_age = input()

age = int(your_age)

if (age >= 1 and age <= 18):
    print('Happy birthday!')
elif(age == 21 or age == 50):
    print('Important birthday!')
elif(age >= 60):
    print('Don\'t retire. Keep working!')
else:
    print('Keep living and help others!')
      