

a,b = (0,1)
count = 0
while count < 10:
    print a,
    t = a + b
    a = b
    b = t
    count +=1
