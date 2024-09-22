"""https://leetcode.com/problems/construct-smallest-number-from-di-string"""

def findNextLocalMinimaMaxima(start, pattern):
    minima = start
    maxima = len(pattern) + 1
    
    for i in range(start, len(pattern)):
        p = pattern[i]
        if p == "D":
            minima = i + 1
        if p == "I":
            maxima = i + 1
            break
    
    
    for i in range(maxima, len(pattern)):
        p = pattern[i]
        if p == "I":
            maxima = i + 1
        if p == "D":
            break
            
    return (minima, maxima)
        
    
def findPossibleSmallestNumberMatchingPattern(pattern):
    number = ""
    
    digitsSorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start = 0
    try:
        while start <= len(pattern):
            (minima, maxima) = findNextLocalMinimaMaxima(start, pattern)
            for i in range(start, minima + 1):
                last = digitsSorted.pop(minima - i)
                number = number + str(last)
                
            for i in range(minima + 1, maxima):
                last = digitsSorted.pop(0)
                number = number + str(last)
                
            start = maxima
        
        return number
    except Exception:
        return -1
    
    
# Driver Code from here
str1 = "DI"
str2 = "DDD"
str3 = "II"
str4 = "DDDIIIIDDDD"
str5 = "IIIIDDDDIIII"
str6 = "IIIDIDDD"
str7 = "DDII"

print(findPossibleSmallestNumberMatchingPattern(str1))
