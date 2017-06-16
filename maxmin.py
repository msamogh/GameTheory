import numpy as np
import gambit

g = gambit.Game.read_game('hello.nfg')

# For each player, find her strictly dominant strategies, if any
for n in range(len(g.players)):

	minima = []
	minima_index = []

	# For each strategy of player n
	for s in range(len(g.players[n].strategies)):
		cells = []
		for c in g.contingencies:
			if c[n] == s:
				cells.append(c)

		minimum = float('inf')
		minimum_index = -1
		for c in cells:
			if float(g.__getitem__(c)[n]) < minimum:
				minimum = float(g.__getitem__(c)[n])
				minimum_index = c

		minima.append(minimum)
		minima_index = minimum_index

	print 'Maxmin of player', n, 'is', max(minima), '- strategy', minima_index[n]
