
from ctypes import pointer


def binarySearch(list, inputs):
    pointer1 = 0
    pointer2 = len(list)-1
    while pointer1 <= pointer2:
        midPointer = round((pointer1 + pointer2)/2)
        if list[midPointer] == inputs:
            return True
        if list[midPointer]  > inputs:
            pointer2 = midPointer - 1
        else:
            pointer1 = midPointer + 1
        # print(pointer1)
        # print(pointer2)

    if pointer1 > pointer2:
        return False
    
numList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
names = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binarySearch(numList, 31))
print(binarySearch(numList, 77))
print(binarySearch(names, "Delta"))

