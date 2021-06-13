


def firstNonRepeatingCharacter(inputString):

	store = dict()
	for x in range(len(inputString) - 1):

		if x in store:
			store[x] += 1
		else:
			store[x] = 1



	return min(store, key=store.get)