class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    char_dict = {}

    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord('a')] += 1
      
      key = tuple(count)
      if key not in char_dict:
        char_dict[key] = []
      char_dict[key].append(s) # tuple because list can't be key

    return list(char_dict.values())