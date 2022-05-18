def main():
    FileRead()
    DemarcationLine()
    LineStrip()
    DemarcationLine()
    CheckFileExtension()
        
def ReadFile(filename):
    files = open(filename)
    lines = files.readlines()
    for index, line in enumerate(lines):
            print(index, "=", line)


def StripFile(filename):
    files = open(filename)
    for lines in files:print(lines.strip())


def RaisingError(filename):
        if filename.endswith(".txt"):
            lines = open(filename)
            for line in lines:print(line.strip())
        else:
            raise ValueError("File must end with .txt")


def FileRead():
    try:
        ReadFile("file.txt") # path is okay, it reads file
    except IOError as e:
        print("Could not open file:", e)


def LineStrip():
        try:
            StripFile("../file.txt")
        except IOError as e:
            print("Could not open file:", e) # it will give error


def CheckFileExtension():
    try:
        RaisingError("file.rtf")
    except IOError as e:
        print("Could not open file:", e)
    except ValueError as e:
        print("Bad Filename:", e)
    
    
def DemarcationLine():
    print("******************")
    
    
if __name__ == "__main__":main()

'''
0 = first line lenore

1 = it is nine, second line and dine

2 = third line and nevermore over

3 = and fourth

4 = fifth pine line lenore

5 = and the tremor

6 = here is more line

7 = and a new line

8 = i love you

9 = where you are staying now?

10 = i don't know
******************
Could not open file: [Errno 2] No such file or directory: '../file.txt'
******************
Bad Filename: File must end with .txt
'''