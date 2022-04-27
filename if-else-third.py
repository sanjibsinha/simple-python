first_name = input("What is your name? \n")
second_name = input("What is his/her name? \n")

two_names = first_name + second_name

both_names_in_lower_case = two_names.lower()

p = both_names_in_lower_case.count("p")
e = both_names_in_lower_case.count("e")
r = both_names_in_lower_case.count("r")
f = both_names_in_lower_case.count("f")
e = both_names_in_lower_case.count("e")
c = both_names_in_lower_case.count("c")
t = both_names_in_lower_case.count("t")

perfect = p + e + r + f + e + c + t

m = both_names_in_lower_case.count("m")
a = both_names_in_lower_case.count("a")
t = both_names_in_lower_case.count("t")
c = both_names_in_lower_case.count("c")
h = both_names_in_lower_case.count("h")

match = m + a + t + c + h

perfect_match = int(str(perfect)) + int(str(match))

if perfect_match < 10 or perfect_match > 90:
    print(f"Your matching count is {perfect_match}, so think again!")
elif perfect_match >= 40 and perfect_match <=50:
    print(f"Your matching count is {perfect_match}, and it's perfect.")
else:
    print(f"Your matching count is {perfect_match}, you can try!")


# Your matching count is 6, so think again!

