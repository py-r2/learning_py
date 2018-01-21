n = range(0,101)

for i in n:
    if i % 3 == 0 and i % 5 == 0:
        n[i] = "FizzBuzz"
    elif i % 3 == 0:
        n[i] = "Fizz"
    elif i % 5 == 0:
        n[i] = "Buzz"
    
print n
