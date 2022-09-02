num = 20
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(num):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
print(loop1())

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < num:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
print(loop2())


def loop1Rec(num, odd_sum = None):
    # Duplicate the loop1 function using recursion
    if num == 0:
        return odd_sum 
    elif odd_sum != None: 
        if num % 2 == 1:
            return loop1Rec(num - 1, odd_sum + num)
        else:
            return loop1Rec(num - 1, odd_sum)

    else:
        odd_sum = 0    
        return loop1Rec(num - 1, odd_sum)
    # if (tempNum < num):
    #     if (tempNum % 2 == 1):
    #         if tempNum == num:
    #             return odd_sum
    #         return loop1Rec(tempNum + 1, odd_sum + tempNum)
    #     else:
    #         return loop1Rec(tempNum + 1, odd_sum)
    # else:
    #     return odd_sum
print(loop1Rec(num))
        
        
    

def loop2Rec(num,even_sum=None):
    # Duplicate the loop2 function using recursion
    if num == 0:
        return even_sum 
    elif even_sum != None: 
        if num % 2 == 0:
            return loop2Rec(num - 1, even_sum + num)
        else:
            return loop2Rec(num - 1, even_sum)

    else:
        even_sum = 0    
        return loop2Rec(num - 1, even_sum)
    # while (num > 0):
    #     if (num % 2 == 0 and num != 20):
    #         return loop2Rec(num-1, even_sum + num)
    #     else:
    #         return loop2Rec(num-1, even_sum)
    # else:       
    #     return even_sum

print(loop2Rec(num))