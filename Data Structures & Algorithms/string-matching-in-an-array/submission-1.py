class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substringArr = []

        for word in words:
            for i in range(len(words)):
                if word in words[i] and word != words[i]:
                    if word not in substringArr:
                        substringArr.append(word)
        return substringArr