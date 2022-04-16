def main():
    x = 1
    print(x)
    print(id(x))
    print(type(x))
    x = 2
    print(x)
    print(id(x))
    print(type(x))
    x = 1
    print(x)
    print(id(x))
    print(type(x))
  

if __name__=="__main__":main()

'''
1
10914496
<class 'int'>
2
10914528
<class 'int'>
1
10914496
'''