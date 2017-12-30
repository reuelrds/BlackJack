import random


class Card(object):
	
	suits="Diamonds Hearts Clubs Spades".split()
	values=range(2,11)+"Ace Joker Queen King".split()
	
	card_values={"Ace":[1,11], "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Joker":10, "Queen":10, "King":10}
	
	def __init__(self,value,suit):
		self.suit=suit
		self.value=value
	
	def show(self):
		print "%s of %s" %(self.value,self.suit)
	
class Deck(object):

	def __init__(self):
		self.deck=[]
		self.build()
	
	def build(self):
		for s in Card.suits:
			for v in Card.values:
				self.deck.append(Card(v,s))
		 
	def shuffle(self):
		random.shuffle(self.deck)
		
	def show(self):
		for card in self.deck:
			card.show()
			
class Dealer(object):

	def __init__(self):
		self.hand=Hand()
	
	def discard(self):
		self.hand.pop()
		
	def shuffle(self):
		Deck.shuffle(d)
		
	def deal(self,d,p): 
		while len(self.hand.hand)!=7:
			self.hand.draw_card(d)
			p.hand.draw_card(d)
			
	def show_hand(self):
		self.hand.show()
	
class Player(object):
	
	def __init__(self,name):
		self.name=name
		self.hand=Hand()
	
	def discard(self):
		self.hand.pop()
			
	def show_hand(self):
		self.hand.show()
		
	def calc_hand_value(self):
		self.hand.hand_value()
		
class Hand(object):
	
	def __init__(self):
		self.hand=[]
	
	def draw_card(self,d):
		self.hand.append(d.deck[random.randint(0,51)])


	def show(self):
		for card in self.hand:
			card.show()
	
	def hand_value(self):
		value=0
		print "rds"
		for c in self.hand:
			value+=Card.card_values[str(self.hand.value)]
		print value

d=Deck()
d.shuffle()

#h=Hand()
#h.draw_card(d)
#h.show()

dele=Dealer()
p=Player("Bob")

dele.deal(d,p)
dele.show_hand()
print ""
p.show_hand()
print ""
for pr in p.hand.hand:
	print Card.card_values[str(pr.value)]
#p.calc_hand_value()


