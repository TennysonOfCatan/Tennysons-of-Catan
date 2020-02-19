

class Player():



    def __init__(self, index):
        #player num
        self.index = index

        #player stats
        self.vp = 0
        self.army = 0
        self.longestRoad = 0

        
        #player resources
        self.wheat = 0
        self.brick = 0
        self.sheep = 0
        self.ore = 0
        self.wood = 0

        #player structures
        self.settlements = 0
        self.cities = 0

        #player deck
        self.cards = []



    #getters
    def getWheat(self):
        return self.wheat

    def getBrick(self):
        return self.brick

    def getSheep(self):
        return sheep

    def getOre(self):
        return self.ore

    def getWood(self):
        return self.wood

    def getLongestRoad(self):
        return self.longestRoad

    def getArmy(self):
        return self.army
    
    def getVP(self):
        return self.vp


    def addCard(self, card):
        self.cards.append(card)

    def buySettlement(self, location):
        if self.sheep < 1 < 1 or self.wheat < 1 or  self.wood < 1 or self.brick < 1:
            Exception("Insufficient resources!")

        else:
            self.wood -= 1
            self.brick -= 1
	    self.wheat -= 1
            self.sheep -=1 
            self.settlements += 1
            self.vp += 1

    def buyCity(self, location):
        if self.settlements < 1 or self.brick < 3 or self.wheat < 2:
            Exception("Insufficient resources.")

        else:
            self.stone -= 3
            self.wheat -= 2
            self.settlements -= 1
            self.cities += 1
            self.vp += 1


    def buyResource(self, card)
        if self.wheat < 1 or self.brick < 1 or self.sheep < 1:
            Exception("Insufficient resource.")

        else:
            self.wheat -= 1
            self.sheep -= 1
            self.brick -= 1
            self.cards.append(card)

    def buyRoad(self):
        if self.brick < 1 or self.wood < 1:
            Exception("Insufficient resource.")

        else:
            self.brick -= 1
            self.wood -= 1

        



    
        

    
