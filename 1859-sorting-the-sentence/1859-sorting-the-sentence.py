class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.strip().split()
        new_list = [0 for i in word_list]
        for word in word_list:
            new_list[int(word[-1])-1] = word[:-1]
        return " ".join(new_list)
