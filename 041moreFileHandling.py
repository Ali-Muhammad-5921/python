with open('myfile.txt','r') as f:
    f.seek(10) # yahan sy reading start hogi
    print(f.tell())# yeh humy btata hy k kaha tk seek kia hua hy
    data = f.read(10)
    print(data)
    #f.truncate(30) jitny characters do gy file ma sirf utny hi character rh jain gy
