class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    final_lst = []
    while strs:
      temp_lst = [strs[0]]
      strs.remove(strs[0])
      for j in strs[:]:
        if sorted(temp_lst[0]) == sorted(j):
          temp_lst.append(j)
          strs.remove(j)
      final_lst.extend([temp_lst])
    return final_lst