

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15}  
    if skus.count("A") > 2:
        for n in range(1, skus.count("A") + 1):
            print(n)
            if n % 3 == 0:
                sum -= 20
                print(sum)
    if skus.count("B") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                sum -= 15
    for item in skus:
        if item in prices:
            sum += prices.get(item)
        else:
            return -1
    return sum

checkout("AAAAAA")