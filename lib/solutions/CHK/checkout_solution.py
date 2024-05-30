

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return -1
    
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
    
    if skus.count("B") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                total -= 15
    
    if skus.count("E") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                total -= 40
    
    for item in skus:
        total += prices.get(item)

    print(total)
    return total

checkout("AA")
checkout("AAAAAAAAAAAAAAA")
checkout("ABCDE")
checkout("AAABBBBBBBCCCDDDE")
checkout("F")
checkout("a")