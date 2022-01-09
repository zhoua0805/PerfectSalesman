def discount_range(increment):
    discount = [i for i in range(0, 100, increment)]
    return discount


# Returns tuple of format (discount, profit)
def find_best_profit_in_range(model, discount_range):
    profit_index = 0

    discount_profit = [(i, model(i)[profit_index]) for i in discount_range]
    discount_profit.sort(key=(lambda x: x[1]), reverse=True)

    return discount_profit[0]
