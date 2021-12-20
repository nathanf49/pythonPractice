def lengthOfLongestSubstring(self, s: str) -> int:
    sub = []  # longest substring
    start = 0  # start of index of longest substring
    maxLen = 0  # len of longest substring
    end = start + maxLen  # index of end of longest substring
    for i in range(len(s)):
        if s[i] not in sub:  # add char to substring, check if there's a new maxLen
            sub.append(s[i])
            if len(sub) > maxLen:  # check to make sure current substring isn't shorter than new one
                maxLen = len(sub)
        else:  # if current char is already in substring
            sub = sub[sub.index(s[i]) + 1:]  # remove current char and all chars before from substring
            sub.append(s[i])  # add new char

    return maxLen