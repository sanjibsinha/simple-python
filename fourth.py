infile = open('file.txt', 'r')
outfile = open('new.txt', 'w')
for line in infile:
    print(line, file=outfile)

print("Done")