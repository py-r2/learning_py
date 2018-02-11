import time
from datetime import datetime as dt
from Tkinter import *

window = Tk()
website_list =[]
def list_update():
    website_list.append(e1_value.get())
    t1.insert(END,e1_value.get()+'\n')
#    return website_list
#    print website_list

b1 = Button(window, text="Block", command=list_update)
b1.grid(row=1,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1,column=1)

t1 = Text(window, height=5, width=20)
t1.grid(row=1,column=2)

l1 = Label(window, text="Enter website:")
l1.grid(row=0,column=1)
l2 = Label(window, text="Websites list blocked:")
l2.grid(row=0,column=2)

window.mainloop()


hosts_temp = r"C:\Users\admin\Documents\GitHub\learning_py\Projects\proj3_website_blocker\hosts"
#hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
#website_list = ["www.facebook.com","www.sistech.ca","facebook.com","sistech.ca"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
#        print "Working hours..."
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.seek(0,2)
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
#        print "Outside business hours..."

    time.sleep(5)
