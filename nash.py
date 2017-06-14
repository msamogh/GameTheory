import numpy as np
import gambit

g = gambit.Game.read_game('hello.nfg')

candidates = {}

# Iterate through the indices of all cells of the payoff matrix
for c in g.contingencies:

	# Iterate through every player for each cell
	for n in range(len(g.players)):

		# Payoff of player n in the current outcome
		payoff = float(g.__getitem__(c)[n])

		# The highest payoff player n can get by deviating only her strategy while others' remain the same
		max_payoff = max([float(g.__getitem__(cprime)[n]) 
							for cprime in g.contingencies 
							if cprime[n] != c[n] and np.count_nonzero(np.array(cprime) - np.array(c)) == 1
						])

		if payoff >= max_payoff:
			candidates[n] = [c] if n not in candidates else candidates[n] + [c]

# Find all common outcomes in the list of candidates for each player (intersection)
equilibria = reduce(set.intersection, 
					[set([tuple(x) for x in candidates[i]]) for i in candidates], 
					set([tuple(x) for x in g.contingencies])
					)

print(list(equilibria))
