"""You are given an array "height" of integers of length n.
There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the maximum water."""

def maximumContainerArea(heights):
    i = 0
    j = len(heights) - 1
    maximumContainerArea = 0

    while i < j:
        leftPillarHeight = heights[i]
        rightPillarHeight = heights[j]

        containerWidth = j - i
        containerHeight = min(leftPillarHeight, rightPillarHeight)
        containerArea = containerWidth * containerHeight
        maximumContainerArea = max(maximumContainerArea, containerArea)

        if leftPillarHeight <= rightPillarHeight:
            i = i + 1
        
        if rightPillarHeight <= leftPillarHeight:
            j = j - 1

    return maximumContainerArea

print(maximumContainerArea([1,8,6,2,5,4,8,3,7]))