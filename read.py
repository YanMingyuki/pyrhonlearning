# import os
# print(os.getcwd)

fq = open("abcd.txt","r")
tmp = fq.readline()
# tmp1 = tmp.replace("\n","")
# tmp2 = tmp1.split(",")
# print(tmp2) 


while tmp != "":
    tmp = fq.readline()
    a = tmp.replace(",","")
    c = b[2].split("/") 
    sum1 = 0
    total = str(c[0])+str(c[1])+str(c[2])
    for i in total:
        sum1=sum1+int(i)
    if sum1>=10:
        sum2=sum1//10
        sum3=sum1%10
        sum1=sum2+sum3
    print(b[0],sum1)
    fq1 = open("/python/test/aaa/bbb.txt","a")
    fq1.write(str(b[0])+" "+str(sum1)+"\n")
    fq1.close().replace("\n","")
    b = a.split()
fq.close()