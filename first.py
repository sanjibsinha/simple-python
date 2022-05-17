import re
def main():
    ReplaceWord()
    DemarcationLine()
    MatchAndReplaceWord()
    
def ReplaceWord():
    files = open("file.txt")
    for line in files:
        
        print(re.sub('lenor|more', "#####", line), end=' ')
            
        
    
def MatchAndReplaceWord():
    files = open("file.txt")
    for line in files:
            match = re.search('(len|neverm)ore', line)
            if match:
                print(line.replace(match.group(), "#####"), end=' ')
                
    
def DemarcationLine():
    print("*************")

if __name__ == "__main__": main()