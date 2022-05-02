class Human:
    def __init__(self, kind = "Good"):
        self.kind = kind
    def whatKind(self):
        return self.kind
def main():
    GoodHuman = Human()
    print(f"A Good human is {GoodHuman.whatKind()}")
    BadHuman = Human("Bad")
    print(f"A Bad human is {BadHuman.whatKind()}")
        
if __name__ == "__main__": main()

'''
A Good human is Good
A Bad human is Bad
'''