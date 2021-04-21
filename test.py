# a = [30,40,50,60,70]                        #每一個元素必須視同一個資料型別

# a.append(90)                                #append在串列後方加入資料
# a.append(100)

# a.insert(4,8)                               #insert在指定位置加入資料

# a.remove(30)                                #刪除指定數值的資料,相同資料只會刪除一筆

# del a[1]                                    #del刪除指定位置的資料

# for i in range(len(a)):                     #逐一顯示串列數字
#     print(a[i])


# b = list("2358")                              #list()輸入字串會逐一分割,如列子會為"2","3","5","8"
# c = list(input("please your number: "))       #猜數字遊戲
# A=0
# B=0
# for i in range(len(b)):
#     for j in range(len(c)) :
#         if j == i and b[i] == c[j]:
#             A+=1
#             break
#         elif b[i] == c[j] :
#             B+=1
#             break
# print(A,"A",B,"b")


# b = int(input("year:"))                          #十二生肖
# y = b % 12-4
# a = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","moneky","rooster","dog","pig"]
# print(a[y])


# a = [6,8,3,4,2,9,1,7]
# a.sort()                                           #順序排列資料
# for i in range(len(a)):
#     print(a[i])


# a = [6,8,3,4,2,9,1,7]                                #泡沫排序法(Bubble sort)
# i=0
# for j in range(len(a)-2):
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             b = a[i]
#             a[i] = a[i+1]
#             a[i+1] = b
            
# print(a)

a=list(input("輸入4個數字:"))
z=a
for j in range(len(a)-2):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b
d=""
for c in range(len(a)):
    d = str(d) + str(a[c])  
print(d)
for x in range(len(z)-1):
    for y in range(len(z)-1):
        if z[y]<z[y+1]:
            b = z[y]
            z[y] = z[y+1]
            z[y+1] = b

f=""
for e in range(len(z)):
    f = str(f) + str(z[e]) 
print(f)
print(int(d)-int(f))