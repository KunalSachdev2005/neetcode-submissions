class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        
        for word in strs:
            final_str = final_str + str(len(word)) + "$" + word
        
        return final_str

    def decode(self, s: str) -> List[str]:
        word_list = []
        i = 0

        while i < len(s):
            # read number's length
            j = i
            while s[j] != "$":
                j += 1
            
            number = int(s[i:j])

            # skip $
            j += 1

            # extract word
            word = s[j:j+number]
            word_list.append(word)

            # move i forward
            i = j + number
        
        return word_list
