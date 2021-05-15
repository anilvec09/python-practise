def isAlienSorted(words, order):
    alien_dict = {v: i for i, v in enumerate(order)}
    # print(alien_dict)
    # print(sorted(words, key=lambda s: [alien_dict[c] for c in s]))
    # print([alien_dict[c] for c in words[0]])
    return words == sorted(words, key=lambda s: [alien_dict[c] for c in s])


assert isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz") == True
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
assert isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz") == False
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

