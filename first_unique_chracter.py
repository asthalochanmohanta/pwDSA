def firstUniqChar(s):

    char_freq = {}
    
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i
    
    return -1

s1 = "leetcode"
print(firstUniqChar(s1))  

s2 = "loveleetcode"
print(firstUniqChar(s2))  

s3 = "aabb"
print(firstUniqChar(s3)) 
