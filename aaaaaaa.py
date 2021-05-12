import os
print(os.getcwd())

fp=open('test2.csv','r')
tmp=fp.readline()

class Classroom:
    def __init__(self):
        self.cla=[]
        self.id=[]
        self.name=[]
        self.git=[]

myclass=Classroom()
while True:
    tt=fp.readline().replace("\n","").replace(" ","")
    if tt==",,,":
        break
    else:    
        tmp=tt.replace("?","").split(",")
        print(tmp)
        myclass.cla.append(tmp[0])
        myclass.id.append(tmp[1])
        myclass.name.append(tmp[2])
        myclass.git.append(tmp[3])

fp.close()

for i in range(len(myclass.cla)):
    print(myclass.cla[i],myclass.id[i],myclass.name[i],myclass.git[i])