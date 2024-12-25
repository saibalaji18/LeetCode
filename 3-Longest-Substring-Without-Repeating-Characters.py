class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}  # Store the last index of each character
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Result variable to store the max substring length

        for right, value in enumerate(s):
            if value in index and index[value] >= left:
                #print(f\left - {left}   |||   right - {right}\)
                #print(f\index - {index}\)
                #print(f\value - {value}\)
                #print(f\index_value - {index[value]}\)
                left = index[value] + 1  # Move the left pointer to avoid duplicates
            index[value] = right  # Update the character's last seen index
            max_length = max(max_length, right - left + 1)  # Update the max length

        return max_length