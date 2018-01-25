def fibon():
    n = int(raw_input('Please enter a number till you want Fibonacci sequace to be printed out to:'))
    a,b = (0,1)
    if n == 0:
        print a
    elif n == 1:
        print a,b
    else:
        for i in range(n):
            a,b = b,a+b
            print a,
fibon()
'''a,b = (0,1)
count = 0
while count < 10:
    print a,
    t = a + b
    a = b
    b = t
    count +=1
'''
