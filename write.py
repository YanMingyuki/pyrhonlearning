import os
print(os.getcwd)

fq = open("/python/test/aaa/bbb.txt","w")
fq.write("name,number\n")
fq.close()