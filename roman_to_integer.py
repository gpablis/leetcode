# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 2 -> II
# 12-> XII, X + II
# 27-> XXVII, XX + V + II

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Testcase 1
# s = "II"

# Testcase 2
# s = "LVIII"

# Testcase 4
s = "MCMXCIV"

def romanToInt(s: str) -> int:
    num = 0
    if s in roman:
        print(roman[s])
    else:
        for i in range(0,len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
    
    return num

number = romanToInt(s)
print(number)