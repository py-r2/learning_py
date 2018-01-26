numbers = [1,2,3]
filename = open('numbers.txt','w')
for i in numbers:
    write = filename.write(str(i)+'\n')
filename.close()
