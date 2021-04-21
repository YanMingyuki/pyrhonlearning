class Person:     #定義類別(由函數及類別所組成)
    def __init__(self,name,weight,hp,ap):
        self.name=name
        self.weight = weight
        self.hp = hp
        self.ap = ap 


    def eat(self):
        self.weight = self.weight+2
        
    def runa(self):
        self.weight = self.weight-1

    def underattack(self,who):
        self.hp = self.hp - who.ap
    
    def attack(self,who):
        who.hp = who.hp - self.ap

handsome = Person("aaa",85,2000,100)  #建立物件 

bbb = Person("bbb",50,1000,50) 

print(handsome)
#handsome.test()      #對指向的物件執行函數
handsome.eat()
handsome.underattack(bbb)
handsome.attack(bbb)
print(handsome.name)
print(handsome.weight)
print(handsome.hp)


print(bbb)
print(bbb.name)
print(bbb.weight)
print(bbb.hp)