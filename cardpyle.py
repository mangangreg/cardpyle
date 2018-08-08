####### Static stuff first #######

# A master list of the standard playing card cards
card_list = []
for suit in ['h','d','c','s']:
	for no in ['A'] + list(range(2,11)) + ['J','Q','K']:
		card_list.append([no,suit])

# Suit lookup dictionary
suit_lookup = {'h': 'Hearts', 'd':'Diamonds', 's':'Spades', 'c':'Clubs'}

# Card (no.) lookup dictionary
card_name = {'J':'Jack','Q':'Queen','K':'King','A':'Ace'}
for i in range(2,11):
	card_name[str(i)]=str(i)
	
# Card index lookup dictionary
card_lookup = {}
for i,c in enumerate(card_list):
	card_lookup[i] = c


class Card:
	'''
	A class that represents a single card
	'''
	def __init__(self, no, suit):
		# The card number
		self.no = str(no).upper()
		
		# The card suit
		self.suit = suit
		
		# Whether the card is face_up or not
		self.face_up = False

	def __str__(self):
		return "The {0} of {1}".format(card_name[self.no], suit_lookup[self.suit])

	def flip(self):
		self.face_up = not(self.face_up)




class Pile:
 	''' A pile takes a list of cards

 	'''

 	def __init__(self,cards=[]):
 		for c in cards:
 			if not(isinstance(c,Card)):
 				print("Error!")
 				break

 		self.size=len(cards)

 		# The top card
 		try:
 			self.top = cards[0]
 		except:
 			self.top = None
 		
 		# The list of cards
 		self.cards = cards

 	def __str__(self):
 		''' Defines what happens when you apply the print function
 		'''
 		for card in self.cards:
 			print(card)
 		return "(That's all of em!)"



 	def shuffle(self,silent = False):
 		import random
 		random.shuffle(self.cards)

 		if silent == True:
 			pass
 		else:
 			return self


 	def shuffled(self):
 		import random
 		random.shuffle(self.cards)


 	def flip_all(self):
 		for card in self.cards:
 			card.flip()
 		
 	def draw(self,k=1):
 		draw = self.cards[0:k]
 		self.cards = self.cards[k:]
 		return draw









def fresh_deck():
	'''
	Returns a full, new, unshuffled deck
	'''
	
	return Pile([Card(c[0],c[1]) for c in card_list])


def random_cards(n=1,replace=False):
	import numpy as np

	pick = np.random.choice(range(52),size=n,replace=replace)

	return [Card(card_lookup[i][0],card_lookup[i][1]) for i in pick]

def random_card():
	import numpy as np
	pick = np.random.randint(0,52)
	c = card_lookup[pick]
	return Card(c[0],c[1])


class Game:
	pass