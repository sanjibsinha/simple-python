import re

def main():
    CompilerAndReplaceWord()

def CompilerAndReplaceWord():
    files = open("file.txt")
    pattern = re.compile('(len|neverm)ore', re.IGNORECASE)
    for line in files:
        if re.search(pattern, line):
            print(pattern.sub("---", line), end=' ')
    

if __name__ == "__main__": main()

'''
first line ---
 third line and --- over
 fifth pine line ---
'''