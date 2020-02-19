import random

class Deck():
#deck has 14 knights, 2 monopolies, 2 plenty years, 2 roads, and 5 world wonders
    
    def __init__(self):

        self.deck = []

        for i in range(0,14)
            knight = Knight()
            self.deck.append(knight)

        for i in range (0, 2):
            monopoly = Monopoly()
            self.deck.append(monopoly)

        for i in range(0,2):
            yearOfPlenty = YearOfPlenty()
            self.deck.append(yearOfPlenty)

        for i in range(0,2)
            roadBuilder = RoadBuilder()
            self.deck.append(roadBuilder)

        for i in range(0,5):
            worldWonder = WorldWonder()
            self.deck.append(worldWonder)


        def shuffle(self):
            random.shuffle(self.deck)

        def draw(self):
            if len(self.deck) < 1:
                Exception("Insufficient cards.")

            card = self.deck.pop()
            return card


        @todo
        #DOES one add a card back to the deck in SoC???
        #No - Lauekat, MetricSeconds chat
        #yes, Codi and Destyn
        #def readd(self, card):


        












        
            





            
