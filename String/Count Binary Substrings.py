# Given a string containing 0s and 1s only
# Find total number of substrings present in a string that satisfy the following conditions:
    # all 0s and 1s are grouped consecutively (eg: 01, 100, 11111100, 00000111)
    # number of 0s is equal to the number of 1s

def countBinarySubstrings(s):
    i = 0
    kind = s[0]
    sameKind = 0
    sameKindEnded = False
    differentKind = 0

    res = 0
    while i < len(s):
        c = s[i]
        if sameKindEnded:
            if c != kind:
                differentKind += 1

                if differentKind == sameKind or i == len(s) - 1:
                    res += differentKind
                    sameKindEnded = False
                    differentKind = 0

                    if kind == "0":
                        kind = "1"
                    else:
                        kind = "0"

                i += 1
            else:
                res += differentKind
                sameKind = differentKind
                sameKindEnded = False
                differentKind = 0

                if kind == "0":
                    kind = "1"
                else:
                    kind = "0"
        else:
            if c == kind:
                sameKind += 1
                i += 1
            else:
                sameKindEnded = True

    return res


# Driver Code from here
str1 = "01"
str2 = "010101"
str3 = "0011"
str4 = "00001111"
str5 = "11000110100"
str6 = "10"
str7 = "111111"
str8 = "0011100"


print(countBinarySubstrings(str1))


