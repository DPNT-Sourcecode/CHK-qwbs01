# import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    
    total = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15, "E": 40, "F":10, "G": 20, "H": 10, "I": 35, "J":60, "K":70, "L":90, "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50, "S":20, "T":20, "U":40, "V":50, "W":20, "X":17, "Y":20, "Z":21} 
    
    for item in skus:
        if item not in prices:
            return -1

    counts = {}
    for item in skus:
        counts[item] = skus.count(item)
    print(counts)

#A
    a_count = skus.count("A")
    while a_count > 0:
        if a_count >= 5:
            total -= 50
            a_count -= 5
        elif a_count >= 3:
            total -= 20
            a_count -= 3
        else:
            break

#B & E
    b_count = skus.count("B")
    e_count = skus.count("E")


    if e_count > 1 and b_count > 0:
        while e_count >= 2 and b_count > 0:
            total -= 30
            e_count -= 2
            b_count -= 1
    
    while b_count >= 2:
        total -= 15
        b_count -= 2

#F
    f_count = skus.count("F")

    while f_count >= 3:
        total -= 10
        f_count -= 3

#H
    while counts.get("H", 0) >= 10:
        total -= 20
        counts["H"] -= 10
    while counts.get("H", 0) >= 5:
        total -= 5
        counts["H"] -= 5

#K
    while counts.get("K", 0) >= 2:
        total -= 10
        counts["K"] -= 2

#N
    while counts.get("M", 0) >= 1 and counts.get("N", 0) >= 3:
        total -= 15
        counts["M"] -= 1
        counts["N"] -= 3
#P
    while counts.get("P", 0) >= 5:
        total -= 50
        counts["P"] -= 5
#Q & R
    while counts.get("R", 0) >= 3 and counts.get("Q", 0) >= 1:
        total -= 30
        counts["R"] -= 3
        counts["Q"] -= 1
    
    while counts.get("Q", 0) >= 3:
        total -= 10
        counts["Q"] -= 3

#U
    while counts.get("U", 0) >= 4:
        total -= 40
        counts["U"] -= 4
#V
    while counts.get("V", 0) >= 3:
        total -= 20
        counts["V"] -= 3
    while counts.get("V", 0) >= 2:
        total -= 10
        counts["V"] -= 2

# STXYZ
    while sum(counts.get("S", 0) + counts.get("T", 0) + counts.get("X", 0) + counts.get("Y", 0) + counts.get("Z", 0)):
    #calc the discount each time, find actual value of group

    for item in skus:
        # print(prices.get(item))
        total += prices.get(item)

    print(skus, total)
    return total

# checkout("EEB") #should be 80
# checkout("EEEB") #should be 120
# checkout("EE") #should be 80
# checkout("EEEEBB") #should be 160
# checkout("ABCDEABCDE") #should be 280
checkout("RRRQ") #should be 150 not 180
checkout("RRRRRRQQ") #should be 300 not 330
checkout("RRRQRQRR") #should be 300 not 330



