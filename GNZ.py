

class Company:
    def __init__(self):
        self.SNHgroup = None

class SNHgroup:
    def __init__(self,name):
        self.name = name
        self.Group = None

class Group:
    def __init__(self,group):
        self.group = group
        self.GNZ = None

class GNZ:
    def __init__(self,team):
        self.team = team
        self.teamNII = None

class TeamNII:
    def __init__(self,name):
        self.jing = None
        self.name = name

class Jing:
    def __init__(self,nm,pd,ut):
        self.nm = nm
        self.pd = pd
        self.ut = ut

Star48 = Company()
Star48.SNHgroup = SNHgroup("SNHgroup")
Star48.SNHgroup.group = Group(["SNH","GNZ","CKG"])
Star48.SNHgroup.group.GNZ = GNZ(["teamG","teamNIII","teamZ"])
Star48.SNHgroup.group.GNZ.teamNII = TeamNII(["jing","xixi"])
Star48.SNHgroup.group.GNZ.teamNII.jing = Jing("lu-jing","SNH 6","my boy")
print(Star48.SNHgroup.group.GNZ.teamNII.jing)