class Card:
	def __init__(self, no, suit):
		self.no = str(no).upper()
		self.suit = suit_map(suit)
		self.face_up = False

	def __str__(self):
		return "The {0} of {1}".format(self.no, suit_map(self.suit))

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
 			out.append(card.suit+ "," + card.no + "\n")
 		return "".join(out)



 	def shuffle(self):
 		import random
 		random.shuffle(self.cards)

 	def random_deck():
 		self.cards = fresh_deck()
 		self.shuffle()

	
 class 


def fresh_deck():
	'''
	Returns a full, new, unshuffled deck
	'''
	card_list = []

	for suit in ['h','d','c','s']:
		for no in ['A'] + list(range(2,11)) + ['J','Q','K']:
			card_list.append(Card(suit,no))
	return Pile(card_list)


 # class Hand:

 # 	def __init__(self,cards=[]):

