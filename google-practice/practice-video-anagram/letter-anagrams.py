def counter(sentence):
	manual = {}
	for i in sentence:
		if i not in manual:
			manual[i] = 0
		manual[i] += 1

	return manual

def comparer(dict1, dict2):
	for letter in dict2.keys():
		# print letter, dict1[letter], dict2[letter]
		if letter not in dict1.keys() or dict2[letter] != dict1[letter]:
			print "Not enough, you need more " + letter + "'s!"
			return
	print "Great, we can start printing now!"

dict1 = counter('aabcdddd')
dict2 = counter('aabcdddd')

comparer(dict1, dict2)

dict1 = counter('aabcdddd')
dict2 = counter('Aaabcdddd')

comparer(dict1, dict2)

dict1 = counter('aabcdddd')
dict2 = counter('aabbcdddd')

comparer(dict1, dict2)



