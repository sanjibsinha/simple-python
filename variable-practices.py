# suppose you will live 175 years

how_old_are_you = input("How old are you?")

print(type(how_old_are_you))


how_many_years_remaining = 175 - int(how_old_are_you)
how_many_months_remaining = how_many_years_remaining * 12
how_many_weeks_remaining = how_many_years_remaining * 52
how_many_days_remaining = how_many_years_remaining * 365
# assuming there will be no leap years :)

print(f"You will still live {how_many_months_remaining} months, " + 
      f"{how_many_weeks_remaining} weeks, " 
      + f"and {how_many_days_remaining} days. Cheers!")


'''
You will still live 1860 months, 8060 weeks, and 56575 days. Cheers!
'''

