D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abppplee"
# Greedy ALgorithm
def find_longest_subs(D, S):
	matches = True
	max_word = ""
	for a in D:
		i = 0
		j = 0
		while i < len(a) and j < len(S):
			if a[i] == S[j]:
				i += 1
				matches = True
			else:
				matches = False
			j+= 1
		if matches and len(a) > len(max_word):
			max_word = a

	return max_word

print "The longest subsequence"
print find_longest_subs(D, S)