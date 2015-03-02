import random 
import math
import itertools
from collections import defaultdict

"""
This is our own code that we have tried making before looking at the solution, we have gotten some help from the WWW ofc.
This code is missing some key elements like being able to sort the winning hand, for example it will put out [4D, 8H,, 7D, AC, 4S] instead of [4D, 4S, AC, 8H, 7D]."""

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    print hands
    print "Vinner:"
    return allmax(hands, key = hand_rank)

def allmax(iterable, key=lambda x:x):
    "Return a list of all items equal to the max of the iterable."
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

def winning_hands(hands):
	result = []
	max_hand = max(hands, key = hand_rank)
	
	for hand in hands:
		if hand_rank(max_hand) == hand_rank(hand):
			result.append(hand)
	return result
	
def hand_rank(hand):
	suits = [s for r, s in hand]
	nr_dif_suits = len(set(suits))

	ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
	ranks.sort(reverse = True)
	nr_dif_ranks = len(set(ranks))
	if ranks == [14, 5, 4, 3, 2]:
		ranks = [5, 4, 3, 2, 1]

	flush = (nr_dif_suits == 1)
	straight = (ranks == range(ranks[0], ranks[0] -5, -1) )

	if flush and straight:
		return (8, max(ranks))
	
	elif ranks.count(ranks[2]) == 4:
		return (7, ranks[2])
	
	elif ranks.count(ranks[2]) == 3 and nr_dif_ranks == 2:
		return (6, ranks[2])
	
	elif flush:
		return (5, )+ tuple(ranks)
	
	elif straight:
		return (4, max(ranks))
	
	elif ranks.count(ranks[1]) == 2 and ranks.count(ranks[3]) == 2:
		max_pair = max(ranks[1], ranks[3])
		min_pair = min(ranks[1], ranks[3])
		other_card = [r for r in ranks if(r != min_pair and r != max_pair)][0]
		return (2, max_pair, min_pair, other_card)
	
	elif nr_dif_ranks == 4:
		the_pair = [r for r in ranks if ranks.count(r) == 2][0]
		other_card = [r for r in ranks if r != the_pair]
		return (1, the_pair)+tuple(other_card)
	
	else:
		return (0, ) + tuple(ranks)

def group(items):
    "Return a list of [(count, x)...], highest count first, the highest x first"
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def unzip(pairs):
    return zip(*pairs)

def card_ranks(cards):

	ranks = []

	for r, s in cards:
		if r == "T":
			ranks.append(11)
		elif r == "Q":
			ranks.append(12)
		elif r == "K":
			ranks.append(13)
		elif r == "A":
			ranks.append(14)
		else:
			ranks.append(int(r))
	ranks.sort(reverse = True)

	return ranks

def straight(ranks):
	return sorted(ranks, reverse=True)==ranks and len(set(ranks))==len(ranks)
	
def flush(hand):
	return [ e[1] for e in hand] == [hand[1][1] for e in range (len(hand))]

def two_pair(ranks):
	t = []
	for r in set(ranks):
		if ranks.count(r) == 2:
			t.append(r)
		if len(t) == 2:
			return tuple(t)
	else:
		return None

def kind(n, ranks):
	if (len(set(ranks)) == (5-n) or len(set(ranks)) == (4-n)):
		if (ranks[0] == ranks[4-n] or ranks[1] == ranks[4-n]):
			return ranks[0]
		else:
			return ranks[4]
	else:
		return None

deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n = 5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Return a list of numhands hands consisting of n cards each"
    random.shuffle(deck)
    deck = iter(deck)
    return [[next(deck) for card in range(n)] for hand in range(numhands)]

""" 
From here in downwards, we have copied the code from Udacity because the task says to copy the shuffle functions from Udacity.
"""

def hand_percentages(n = 700*1000):
    "Sample n random hands and print a table of percentages for each type of hand"
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n))

def all_hand_percentages():
    "Print an exhaustive table of frequencies for each type of hand"
    counts = [0]*9
    n = 0
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    for hand in itertools.combinations(deck, 5):
        n += 1
        ranking = hand_rank(hand)[0]
        counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %7d %6.3f'%(hand_names[i], counts[i], 100.*counts[i]/n))

def shuffle1(deck):
    # O(N**2)
    # incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    # O(N**2)
    # incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]        

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)

print poker(deal(3))
