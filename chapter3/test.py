def main():
    print('A line inside main function.')
        
    print("A line outside main function.")
    OutsideMainFunction()
    
def OutsideMainFunction():
        x = 0
        while x < 5:
            print(x)
            x = x + 1    

if __name__=="__main__":main()

## A line inside main function.
# A line outside main function.
# 0
# 1
# 2
# 3
# 4
