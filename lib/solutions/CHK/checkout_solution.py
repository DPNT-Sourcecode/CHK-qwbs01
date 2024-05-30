

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15, "E": 40}  
    a_count = 0
    a_count = skus.count("A")
    if len(skus) == 0:
        return -1
    while a_count > 0:
        print(a_count)
        if a_count % 5 == 0:
            sum -= 50
            a_count -= 5
        elif a_count % 3 == 0:
            sum -= 20
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
    return print(sum)

checkout("AAAAA")

