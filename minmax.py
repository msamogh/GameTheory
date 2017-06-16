import numpy as np
import gambit

g = gambit.Game.read_game('hello.nfg')

for n in range(len(g.players)):

	maxima = []
	maxima_index = -1

	for c in g.contingencies:
		maximum = -float('inf')
		maximum_index = -1

		for s in range(len(g.players[n].strategies)):
			if g.__getitem__(c[:n] + [s] + c[n+1:])[n] > maximum:
				maximum = float(g.__getitem__(c[:n] + [s] + c[n+1:])[n])
				maximum_index = c

		maxima.append(maximum)
		maxima_index = maximum_index

	print 'Minmax of player', n, 'is', min(maxima), '- strategy', maxima_index[maxima.index(min(maxima))]