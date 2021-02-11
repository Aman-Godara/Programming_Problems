"""Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in the input array.
Consider -1 as the next greater element for an element for which no NGE exists.

In the same way calculate NSE (Next Smaller Element)"""


def nextGreater(arr):
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        added_current = False
        while stack:
            face = stack.pop()
            if current < face:
                stack.append(face)
                stack.append(current)
                added_current = True
                print(str(current) + ':', face)
                break
        if not added_current:
            stack.append(current)
            print(str(current) + ':', -1)


nextGreater([1, 3, 2, 4, 12, 12, 3, 24, 5, 2, 5])


def nextSmaller(arr):
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        next_smaller = -1
        while stack:
            face = stack.pop()
            if current > face:
                stack.append(face)
                next_smaller = face
                break
        stack.append(current)
        print(str(current) + ':', next_smaller)


nextSmaller([1, 3, 2, 4, 12, 12, 3, 24, 5, 2, 5])
