import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    
    total = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15, "E": 40}  
    
    for item in skus:
        if item not in prices:
            return -1

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
    
    if skus.count("B") > 1 and skus.count("E") < 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                print("Dicount B 15 triggered")
                total -= 15
    
    # if skus.count("E") > 1:
    #     for m in range(1, skus.count("B") + 1):
    #         if m % 2 == 0:
    #             total -= 30
    if skus.count("E") > 1 and skus.count("B") > 0:
        print(skus.count("B"))
        for _ in range(1, skus.count("B") + 1):
            print("Dicount E 30 triggered")
            total -= 30
            # print(total)
    
    for item in skus:
        # print(prices.get(item))
        total += prices.get(item)

    print(skus, total)
    return total

# checkout("EEB") #should be 80
# checkout("EEEB") #should be 120
# checkout("EE") #should be 80
# checkout("EEEEBB") #should be 160
checkout("ABCDEABCDE") #should be 280


