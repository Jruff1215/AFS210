from random import randint

def shuffle(list):
    cache = {}
    for i in range(0, len(list) - 1):
        if cache.get(str(i)) is None:
            new = randint(i, len(list)-1)
            while cache.get(str(new)) is not None:
                new = randint(i, len(list)-1)

            cache[str(new)] = list[i]
            cache[str(i)] = list[new]
            num1 = list[i]
            num2 = list[new]
            list[i] = num2
            list[new] = num1
            #print(new)
    print(list)
    return list
list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(list)
print("Shuffled")
shuffle(list)
shuffle(list)
shuffle(list)
shuffle(list)
shuffle(list)
