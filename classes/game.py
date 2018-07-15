import random

class bcolors:
    HEADER = "\003[95m"
    OKBLUE = "\003[94m"
    OKGREEN = "\003[92m"
    WARNING = "\003[93m"
    FAIL = "\003[91m"
    ENDC = "\003[0m"
    BOLD = "\003[1m"
    UNDERLINE = "\003[4m"

class Person:
    def __init__(self,healthPoint, mainPoint, attack, defense, magic):
        self.maxHp = healthPoint
        self.healthpoint = healthPoint
        self.maxMp = mainPoint
        self.mainPoint = mainPoint
        self.attackLow = attack - 10
        self.attackHigh = attack + 10
        self.defense = defense
        self.magic = magic
        self.actions = ["Attack","Magic"]

    def generateDamage(self):
        return random.randrange(self.attackLow,self.attackHigh)

    def generateMagicDamage(self,i):
       mgLow = self.magic[i]["dmg"] - 5
       mgHigh = self.magic[i]["dmg"] + 5
       return random.randrange(mgLow,mgHigh)

    def takeDamage(self,dmg):
        self.healthpoint = self.healthpoint-dmg
        if(self.healthpoint<0)
            self.healthpoint = 0
        return self.healthpoint

    def getHealthPoint(self):
        return self.healthpoint

    def getMaxHp(self):
        return self.maxHp

    def getMainPoint(self):
        return self.mainPoint

    def getMaxMainPoint(self):
        return self.maxMp

    def reduceMainPoint(self,cost):
        self.mainPoint = self.mainPoint - cost

    def getMagicName(self,i):
        return self.magic[i]["name"]

    def getMagicMainPointCost(self,i):
        return self.magic[i]["cost"]

    def chooseAction(self):
        i=1
        for items in self.actions:
            print (str(i)+ ":",)
