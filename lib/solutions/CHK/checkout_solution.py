

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15, "E": 40}  
    # if skus.count("A") > 2:
    #     for n in range(1, skus.count("A") + 1):
    #         if n % 15 == 0:
    #             sum -= 50
    #         elif n% 5 == 0:
    #             sum -= 50
    #         elif n % 3 == 0:
    #             sum -= 20
    a_count = 0
    a_count = skus.count("A")
    while a_count > 0:
        if a_count >= 5:
            sum -= 50
            a_count -= 5
        

    if skus.count("B") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                sum -= 15
    if skus.count("E") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                sum -= 40
    for item in skus:
        if item in prices:
            sum += prices.get(item)
        else:
            return -1
    return sum


