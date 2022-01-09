import torch
import matplotlib.pyplot as pyplot

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

def plotProductTrend(model, product, result, products, discount_range):
    discount_sales = [model(torch.Tensor([d]+pd.get_dummies(pd.Series(products))[product].tolist()))[0] for d in discount_range]
    discount_qty = [model(torch.Tensor([d]+pd.get_dummies(pd.Series(products))[product].tolist()))[1] for d in discount_range]
    discount_profit = [model(torch.Tensor([d]+pd.get_dummies(pd.Series(products))[product].tolist()))[2] for d in discount_range]

    pyplot.plot(discount_range, discount_sales, label='Sales')
    pyplot.plot(result[0], result[1], 'r*')
    pyplot.plot(discount_range, discount_profit, label='Profit')
    pyplot.plot(result[0], result[3], 'r*', label="You are here")
    pyplot.legend()
    pyplot.ylabel('Dollar')
    pyplot.xlabel('% of discount')
    pyplot.title(f'Sales & Profit vs. percentage discount for {product}')
    pyplot.show()
    pyplot.plot(discount_range, discount_qty, label='Qty')
    pyplot.plot(result[0], result[2], 'r*', label="You are here")
    pyplot.legend()
    pyplot.ylabel('Qty')
    pyplot.xlabel('% of discount')
    pyplot.title(f'Qty vs. percentage discount for {product}')
    pyplot.show()
    return