def abcd(a, pattern):
    mn = a
    mx = len(pattern)
    
    for i in range(a, len(pattern)):
        p = pattern[i]
        if p == "M":
            mn = i + 1
        if p == "N":
            mx = i + 1
            break
    
    
    for i in range(mx, len(pattern)):
        p = pattern[i]
        if p == "N":
            mx = i + 1
        if p == "M":
            break
            
    return (mn, mx)
        
    
def findPossibleSmallestNumberMatchingPattern(pattern):
    ans = ""
    
    taken = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = 0
    try:
        while a <= len(pattern):
            (mn, mx) = abcd(a, pattern)
            for i in range(a, mn + 1):
                last = taken.pop(mn - i)
                ans = ans + str(last)
                
            for i in range(mn + 1, mx + 1):
                last = taken.pop(0)
                ans = ans + str(last)
                
            a = mx + 1
        
        return ans
    except Exception as e:
        return -1
    
    
# Driver Code from here
str1 = "MN"
str2 = "MN"
str3 = "MN"
str4 = "MN"
str5 = "MN"
str6 = "MN"
str7 = "MN"

print(findPossibleSmallestNumberMatchingPattern(str1))
