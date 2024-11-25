class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            #print(sorted_word)
            anagram_map[sorted_word].append(word)
            #print(anagram_map)
        
        return list(anagram_map.values())