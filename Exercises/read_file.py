filename = open('fruits.txt','r')
#for line in filename:
#    print(line) + '\n'
content = filename.read()
filename.close()
print content

'''Print out the lenght of each line'''
#content = filename.readlines()
#filename.close()
#for word in content:
#    print (len(word)-1)
