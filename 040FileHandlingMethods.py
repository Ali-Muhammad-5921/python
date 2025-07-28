# it is useful for reading data such as students marks
f = open('myfile.txt','r')
while True:
    line = f.readline()
    if not line :
        break
    print(line)

# we can also write lines 