import sys

try:
    #f = open('file.txt') 
    # # Could not convert data to an integer.
    f = open('filee.txt') 
    # # OS error: [Errno 2] No such file or directory: 'filee.txt'    
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

