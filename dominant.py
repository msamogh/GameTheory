import numpy as np
import gambit

g = gambit.Game.read_game('hello.nfg')

# For each player, find her strictly dominant strategies, if any
for n in range(len(g.players)):

	# For each strategy, check if it is strictly dominant
	for s in range(len(g.players[n].strategies)):

		# Contains payoffs for all contingencies other than the current strategy being checked
		others = [x for x in g.contingencies if x[n] != s] 

		if all([float(g.__getitem__(x)[n]) < float(g.__getitem__(x[:n] + [s] + x[(n+1):])[n]) for x in others]):

			print 'Strategy', s, 'is dominant for player', n

			# Break commented to make change to weakly dominant easy
			# break
