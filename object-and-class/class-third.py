class Bear:
    age = 10
    time = 0
    
    def get_the_present_age(self):
        print(f"My age is {self.age}")
    
    def grow_with_time(self, time):
        self.age = self.age + time
        print(f"I'm growing up. After {time} years, my age is {self.age}")
        
bear = Bear()
bear.get_the_present_age()
bear.grow_with_time(2)

'''
My age is 10
I'm growing up. After 2 years, my age is 12
'''

