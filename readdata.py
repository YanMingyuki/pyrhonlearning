import os

class Classroom:
    def __init__(self):
        self.name = None
        self.student = []
    def add(self,studentdata):
        self.student.append(studentdata)

class Studentdata:
    def __init__(self,classr,num,name,URL):
        self.classr = classr
        self.num = num
        self.name = name
        self.URL = URL
    

locate = os.getcwd()
tmp = open(locate+"/test2.csv")
a = Classroom()
aa = tmp.readline()
while aa!="":
    aa = tmp.readline()
    s = aa.replace("?"," ").split(",")
    if aa=="":
        continue
    if s[3]=="\n":
        s[3] = ""
    else:
        s[3] = s[3].replace("\n","")
    a.add(Studentdata(s[0],s[1],s[2],s[3]))

tmp.close()


for i in a.student :
    print(i.classr,i.num,i.name,i.URL)



