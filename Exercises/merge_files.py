import datetime

content1 = open('file1.txt','r')
content2 = open('file2.txt','r')
content3 = open('file3.txt','r')
filename = datetime.datetime.now()
def create_file():
    with open(filename.strftime('%Y-%m-%d-%H-%M')+'.txt','w') as file:
        file.write(str(content1.read()) + '\n' + str(content2.read()) + '\n' + str(content3.read()))
create_file()
