temperatures=[10,-20,-289,100]
filename = open('temperature.txt','a+')
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        filename.write(str(f)+'\n')
for t in temperatures:
    c_to_f(t)
filename.seek(0)
filename.close()
