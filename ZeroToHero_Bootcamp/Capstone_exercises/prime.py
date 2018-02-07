'''This small program will get an input number from user and will find
all Prime Factors (if there are any) and display them'''

while True:

    num = int(raw_input(
    'Please enter a positive integer number up to which'
    ' you want to have all its Prime Factors displayed on console:'))

    if num < 0:
        print "This is not a positive number. Please try again."
    elif num == 0:
        print num
    else:
        factors = lambda n: [x for x in range(1,n+1) if not n % x]
        is_prime = lambda n: len(factors(n))==2
        primefactors = lambda n: list(filter(is_prime,factors(n)))
        print factors(num)
        print primefactors(num)
        break

#is_prime
#primefactors
        # for i in range(1,num+1):
        #     l = []
        #     if num % i == 0:
        #         l += str(i)
        #         print l
        #break
