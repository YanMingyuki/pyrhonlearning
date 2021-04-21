class Head:
    def __init__(self,size):
        self.size = size

class Body:
    def __init__(self,capacity):
        self.capacity = capacity

class Hand:
    def __init__(self,length):
        self.length = length

class Leg:
    def __init__(self,width):
        self.width = width

class People:
    def __init__(self):
        self.hd = None
        self.bd = None
        self.rh = None
        self.lh = None
        self.rl = None
        self.ll = None

aaa = People()
aaa.hd = Head(30)
aaa.bd = Body(2000)
aaa.rh = Hand(30)
aaa.lh = Head(30)
aaa.rl = Leg(50)
aaa.ll = Leg(50)
