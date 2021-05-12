class Circle:
    def __init__(self,radius:float=1.0):
        self.radius = radius

    def set_radius(self):
        if (self.radius<0):
            print("error")
        else:
            self.radius = radius

    def get_radius(self):
        return self.radius 

    def get_area(self):
        return 3.1415*self.radius*self.radius


class Point:
    def __init__(self,x:int=0,y:int=0):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y

    def mul(self):
        return self.x*self.y


class Rectangle:
    def __init__ (self,longth=0.0,width=0.0):
        self.longth = longth
        self.width = width
    
    def set_rectangle(self):
        if (self.longth>0 and self.width>0):
            self.longth = longth
            self.width = width
        else:
            print("error")

    def get_rectangle(self):
        return self.longth 
        return self.width

    def get_area(self):
        return self.longth*self.width
    
    def get_meter(self):
        return (self.longth+self.width)*2



class Square:
    def __init__ (self,side):
        self.side = side

    def set_side(self):
        if (self.side<0):
            print("error")
        else:
            self.side = side

    def get_side(self):
        return self.side
        
    def get_area(self):
        return self.Side*self.Side
    
    def get_meter(self):
        return self.Side*4