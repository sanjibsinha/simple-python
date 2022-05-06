class Bear:
    age = 0
    
    def get_the_present_age(self, age):
        print(f"My age is {age}")
    
    def grow_with_time(self, age):
        print(f"I'm growing up. My age is {age}")
        
bear = Bear()
bear.get_the_present_age(10)
bear.grow_with_time(11)

'''
My age is 10
I'm growing up. My age is 11
'''