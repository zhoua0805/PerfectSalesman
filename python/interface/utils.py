import torch

def discount_range(increment):
    discount = [i for i in range(0, 100, increment)]
    return discount


# Returns tuple of format (discount, profit)
def find_best_profit_in_range(model, products, discount_range):
    profit_index = 2

    all_combinations = []
    for i in products: 
        for j in discount_range:
            all_combinations.append((i,j))

    discount_profit = [(p, d, model(torch.Tensor([d]+pd.get_dummies(pd.Series(products))[p].tolist()))) for (p, d) in all_combinations]
    discount_profit.sort(key=(lambda x: x[2][profit_index]), reverse=True)

    return discount_profit[0]
