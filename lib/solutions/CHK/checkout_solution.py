

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    prices = {"A":50, "B": 30, "C": 20, "D":15}
    for item in skus:
        if item in prices:
            sum += prices.get(item)
        else:
            return -1  
    if skus.count("A") > 2:
        #calculate discount
        
        pass
    return sum

