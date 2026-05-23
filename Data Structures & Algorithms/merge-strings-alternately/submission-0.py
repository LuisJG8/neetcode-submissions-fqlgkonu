class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, l2 = 0, 0
        final_word = []

        while l < len(word1) and l2 < len(word2):
            final_word.append(word1[l])
            final_word.append(word2[l2])  
            l2 += 1
            l += 1
        final_word.append(word1[l:])
        final_word.append(word2[l2:])

        return "".join(final_word)