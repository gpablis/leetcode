def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        string1 = {}
        for l in s:
            if l in string1:
                string1[l] += 1
            else:
                string1[l] = 1

        string2 = {}
        for l in t:
            if l in string2:
                string2[l] += 1
            else:
                string2[l] = 1

        if string1 == string2:
            return True
        else:
            return False
    else:
        return False

# Testcase 1
# s = "anagram"
# t = "nagaram"

# Testcase 2
# s ="rat"
# t ="car"

# Testcase 3
s = "aacc"
t = "ccac"

print(isAnagram(s,t))