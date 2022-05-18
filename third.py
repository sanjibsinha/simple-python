import re
def main():
    FindWord()
    DEmarcationLine()
    MatchWord()


def FindWord():
    files = open("file.txt")
    for line in files:
        if re.search('lenor|more', line):
            print(line, end=' ')
        
def MatchWord():
    files = open("file.txt")
    for line in files:
        match = re.search('(len|neverm)ore', line)
        if match:
            print(match.group())
        
def DEmarcationLine():
        print("*************")

if __name__ == "__main__": main()

'''
first line lenore
 third line and nevermore over
 fifth pine line lenore
 here is more line
 *************
lenore
nevermore
lenore
'''