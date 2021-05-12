# class Head:
#     def __init__(self,size):
#         self.size = size

# class Body:
#     def __init__(self,capacity):
#         self.capacity = capacity

# class Hand:
#     def __init__(self,length):
#         self.length = length

# class Leg:
#     def __init__(self,width):
#         self.width = width

# class People:
#     def __init__(self):
#         self.hd = None
#         self.bd = None
#         self.rh = None
#         self.lh = None
#         self.rl = None
#         self.ll = None

# aaa = People()
# aaa.hd = Head(30)
# aaa.bd = Body(2000)
# aaa.rh = Hand(30)
# aaa.lh = Head(30)
# aaa.rl = Leg(50)
# aaa.ll = Leg(50)


class Car:
    def __init__(self):
        self.en =None
        self.fr =None
        self.fl =None
        self.br =None
        self.bl =None
class Wheel:
    def __init__(self,size):
        self.size =size
class Engine:
    def __init__(self,cc):
        self.cc =cc

a = Car()
a.en = Engine(2500)
a.fr =Wheel(40)
a.fl =Wheel(40)
a.br =Wheel(40)
a.bl =Wheel(40)

class Car1:
    def __init__(self,size):
        self.en =None
        self.wls =None


cwls=8 #輪胎變數

b=Car()
b.en = Engine(2500)
b.wls =[]
for i in range(cwls):
    tmp =Wheel(50)
    b.wls.append(tmp)