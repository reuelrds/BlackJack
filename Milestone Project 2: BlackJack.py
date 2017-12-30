import random

i=1
class Card(object):
	
	suits="Diamonds Hearts Clubs Spades".split()
	ranks=range(2,11)+"Ace Joker Queen King".split()
	
	card_values={"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Joker":10, "Queen":10, "King":10}
	
	def __init__(self,rank,suit):
		self.suit=suit
		self.rank=rank
	
	def show(self):
		print "%s of %s" %(self.rank,self.suit)
	
class Deck(object):

	def __init__(self):
		self.deck=[]
		self.build()
	
	def build(self):
		for s in Card.suits:
			for v in Card.ranks:
				self.deck.append(Card(v,s))
		 
	def shuffle(self):
		random.shuffle(self.deck)
		
	def show(self):
		for card in self.deck:
			card.show()
			
class Dealer(object):

	def __init__(self):
		self.dealer_hand=Hand()
	
	def discard(self):
		self.dealer_hand.hand.pop()
		
	def shuffle(self,d):
		Deck.shuffle(d)
		
	def deal(self,d,p): 
		while len(self.dealer_hand.hand)!=2:
			self.dealer_hand.draw_card(d)
			p.player_hand.draw_card(d)
			
	def show_hand(self):
		self.dealer_hand.show()
		
	def calc_hand_value(self):
		self.dealer_hand.hand_value()
	
class Player(object):
	
	def __init__(self,name):
		self.name=name
		self.player_hand=Hand()
	
	def discard(self):
		self.player_hand.hand.pop()
			
	def show_hand(self):
		self.player_hand.show()
		
	def calc_hand_value(self):
		self.player_hand.hand_value()
		
class Hand(object):
	
	def __init__(self):
		self.hand=[]
	
	def draw_card(self,d):
		self.hand.append(d.deck.pop(random.randint(0,len(d.deck)-1)))

	def show(self):
		for card in self.hand:
			card.show()
	
	def hand_value(self):
		value=0
		for c in self.hand:
			value+=Card.card_values[str(c.rank)]
		
		#if value<=11 and self.hand.count()>=1:
		#	value+=10
				
		print value
		

def main():
	d=Deck()

	dele=Dealer()
	p=Player("Bob")
	
	dele.shuffle(d)
	dele.deal(d,p)
	print ""
	dele.show_hand()
	print ""
	dele.calc_hand_value()
	print "\n\n"
	p.show_hand()
	print ""
	p.calc_hand_value()
	
	

main()
