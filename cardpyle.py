class Card:
	def __init__(self, no, suit):
		self.no = str(no).upper()
		self.suit = suit_map(suit)
		self.face_up = False

	def __str__(self):
		return "The {0} of {1}".format(card_name[self.no], suit_map(self.suit))

	def flip(self):
		self.face_up = not(self.face_up)

	
def suit_map(s):
	if type(s) != str:
		return 'Error'
	suit = s[0].lower()

	if suit == 'h':
		return "Hearts"
	elif suit == 'd':
		return "Diamonds"
	elif suit == 's':
		return "Spades"
	elif suit == 'c':
		return "Clubs"

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

 		out =[]
 		for card in self.cards:
 			out.append(card.no + "," + card.suit +  "\n")
 		return "".join(out)



 	def shuffle(self):
 		import random
 		random.shuffle(self.cards)

 	def random_deck():
 		self.cards = fresh_deck()
 		self.shuffle()

	


card_list = []
for suit in ['h','d','c','s']:
	for no in ['A'] + list(range(2,11)) + ['J','Q','K']:
		card_list.append([no,suit])

N = len(card_list)

# Lookup card from index
card_lookup = {}
for i,c in enumerate(card_list):
	card_lookup[i] = c

# Lookup suits
card_name = {'J':'Jack','Q':'Queen','K':'King','A':'Ace'}
for i in range(2,11):
	card_name[str(i)]=str(i)



def fresh_deck():
	'''
	Returns a full, new, unshuffled deck
	'''
	
	return Pile([Card(c) for c in card_list])


 # class Hand:

 # 	def __init__(self,cards=[]):

def random_cards(n=1,replace=False):
	import numpy as np

	pick = np.random.choice(range(N),size=n,replace=replace)

	return [Card(card_lookup[i][0],card_lookup[i][1]) for i in pick]

def random_card():
	import numpy as np
	pick = np.random.randint(0,N)
	c = card_lookup[pick]
	return Card(c[0],c[1])