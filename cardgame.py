import random
import time

class Deck:
    #all lists of card
    def __init__(self,cards,discardPile,hand):
        self.cards = cards
        self.discardPile=discardPile
        self.hand=hand


    def deckSize(self):
        return len(self.cards)

    def handSize(self):
        return len(self.hand)

    def discardSize(self):
        return len(self.discardPile)

    #shuffle the deck to randomize it
    def shuffleDeck(self):
        random.shuffle(self.cards)
    
    #removes card from deck and adds it to hand
    def drawCard(self):
        if self.checkIfEmpty():
            self.emptyDeck()
        drawnCard = self.cards.pop(0)
        self.hand.append(drawnCard)
        return drawnCard

    #checks if deck is empty, should be done before drawing.
    def checkIfEmpty(self):
        return len(self.cards) == 0
        #RETURNS TRUE IF DECK IS EMPTY

    #if deck is empty it refills the deck with the discard pile
    def emptyDeck(self):
        print("Deck has no cards, reshuffling deck!")
        self.cards = self.cards+self.discardPile
        random.shuffle(self.cards)
        # print(self.cards)
        self.discardPile = []

    #discards a card from your hand based on zero based index
    def discardCardFromHand(self,cardIndex):
        discardedCard = self.hand.pop(cardIndex)
        self.discardPile.append(discardedCard)
    def discardHand(self):
        self.discardPile = self.discardPile + self.hand
        self.hand = []



    def playCardByIndex(self,cardIndex):
        playedCard = self.hand.pop(cardIndex)
        playedCard.playCard()
        self.discardPile.append(playedCard)

    def playCard(self,card):
        playedCard = self.hand.remove(card)
        playedCard.playCard()
        self.discardPile.append(playedCard)


class Card:
    def __init__(self, name, hp, mp,dmg):
        self.name = name
        self.hp=hp
        self.mp=mp
        self.dmg=dmg

    def playCard(self):
        #unsure what to do here for now. lets just make it print out its stats and discard it
        print("Card Name: "+self.name)
        print("HP: "+str(self.hp)+" MP: "+str(self.mp))
        return self.name, self.hp, self.mp

    def cardCombat(self,enemyCard):
        while self.hp > 0 and enemyCard.hp > 0:
            time.sleep(1)
            print(self.name+" attacks for "+str(self.dmg)+"!!")
            enemyCard.hp-=self.dmg
            time.sleep(1)
            print(enemyCard.name+" attacks for "+str(enemyCard.dmg)+"!!")
            self.hp-=enemyCard.dmg
            print("Player:")
            print(self.name+" HP: "+str(self.hp)+" MP: "+str(self.mp))
            print("Enemy:")
            print(enemyCard.name+" HP: "+str(enemyCard.hp)+" MP: "+str(enemyCard.mp))
        if self.hp>0:
            print("your card won!")
        else:
            print("your enemy prevails!")



c1=Card("Goblin",10,5,1)
c2=Card("hobgoblin",15,5,1)
c3=Card("Wizard",10,5,1)
c4=Card("Potato man",10,5,1)
c5=Card("Green Goblin",10,5,1)
c6=Card("Tumeric monster",10,5,1)
c7=Card("mad pasta",10,5,1)
c8=Card("orange peel garbage",10,5,1)
c9=Card("Gobby",10,5,1)
c10=Card("Grimbo",10,5,1)
c11=Card("Gippy",10,5,1)
c12=Card("grep",10,5,1)

deck = Deck([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[],[])
eDeck = Deck([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[],[])


def gamePlayLoop(deck,eDeck):
    deck.shuffleDeck()
    while True:
        
        print("cards in deck: "+str(deck.deckSize()))
        print("cards in discard: "+str(deck.discardSize()))
        print("you draw 5 cards...")
        for i in range(5):
            deck.drawCard()
        print("your cards: ")

        i=0
        for card in deck.hand:
            print(str(i)+".) "+card.name)
            print("HP: "+str(card.hp)+" MP: "+str(card.mp))
            i+=1

        invalidMove = True
        while invalidMove:
            print("make your move: ")
            print("")
            x = input()
            if int(x)>=0 and int(x)<deck.handSize():
                pCard = deck.hand[int(x)]
                deck.playCardByIndex(int(x))
                
                invalidMove=False
            else:
                print("Invalid move detected!")
        print("move done. discarding hand")
        deck.discardHand()
        print("Enemys turn: ")
        for i in range(5):
            eDeck.drawCard()
        print("enemy is making their move...")
        choice = random.randrange(0,eDeck.handSize())
        print("Enemy plays: ")
        eCard = eDeck.hand[choice]
        eDeck.playCardByIndex(choice)
        pCard.cardCombat(eCard)




gamePlayLoop(deck,eDeck)