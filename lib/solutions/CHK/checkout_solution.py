

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    a_special = 0
    b_special = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15}  
    if skus.count("A") > 2:
        for n in range(1, skus.count("A") + 1):
            if n % 3 == 0:
                sum =- 20
    if skus.count("B") > 1:
        for m in range(1, skus.count("B") + 1):
            if m % 2 == 0:
                sum -= 15
    for item in skus:
        if item in prices:
            sum += prices.get(item)
        else:
            return -1
    print(sum - a_special - b_special)
    return sum - a_special - b_special

checkout("AAA")
checkout("AAAAAA")
checkout("BB")