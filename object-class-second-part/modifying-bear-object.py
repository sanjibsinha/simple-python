class Bear:
    age = 10
    
    def introduce(self, age):
        print(f"I am Bear. I am {age} years old.")
    
    def eat(self):
        print("I am eating.")
        
dad_bear = Bear()
dad_bear.introduce(20)
# I am Bear. I am 20 years old.
child_bear = Bear()
child_bear.introduce(2)
# I am Bear. I am 2 years old.