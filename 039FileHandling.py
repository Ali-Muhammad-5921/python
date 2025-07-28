# f = open('myfile.txt','r') phly file ka naam phr uska mode  ismy hum a likh kr agy msg bhi likh skty hain append krny k liye
#agr write mode ma esi file ko khol diya jo k exist nhi krti to woh create ho jaye gi 


#reading from a file
f = open('myfile.txt','r')
t = f.read()
print(t)
f.close()

# writing to a file 

f = open('myfile.txt','w')
f.write('abc')
f.close()

# is trah append bhi kr skty hain 