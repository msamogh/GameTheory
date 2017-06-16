import numpy as np
import gambit
import sys
import operator

op = {'strict': operator.gt, 'weak': operator.ge, 'vweak': operator.ge}

g = gambit.Game.read_game('hello.nfg')

if len(sys.argv) < 2:
	print 'Format: python dominant.py <strict|weak|vweak>'
else:
	strictness = sys.argv[1]
	
	# For each player, find her strictly dominant strategies, if any
	for n in range(len(g.players)):

		# For each strategy, check if it is strictly dominant
		for s in range(len(g.players[n].strategies)):

			# Contains payoffs for all contingencies other than the current strategy being checked
			others = [x for x in g.contingencies if x[n] != s] 

			if all([op[strictness](g.__getitem__(x)[n], g.__getitem__(x[:n] + [s] + x[n + 1:])[n]) for x in others]):
				
				# If weak, check for at least one strict inequality
				if strictness == 'weak':
					if any([[operator.gt(g.__getitem__(x)[n], g.__getitem__(x[:n] + [s] + x[n + 1:])[n]) for x in others]]):
						print 'Strategy', s, 'is dominant for player', n, 'with strictness level \'' + str(strictness) + '\''

				# Otherwise, no need to check
				else:		
					print 'Strategy', s, 'is dominant for player', n, 'with strictness level \'' + str(strictness) + '\''

		else:
			print 'No dominant strategy for player', n, 'with strictness level \'' + str(strictness) + '\''
