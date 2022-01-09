from PerfectSalesman.python.interface.utils import discount_range
from PerfectSalesman.python.interface.utils import find_best_profit_in_range
from model.Model import Model

def demo():
    # TODO: get current month and decide path
    modelPath = '/content/december.pt'
    model = Model()
    model.load_state_dict(torch.load(modelPath, map_location=torch.device('cpu')))
    products = ["Accessories", "Appliances", "Art", "Binders", "Bookcases", "Chairs", 
              "Copiers", "Envelopes", "Fasteners", "Furnishings", "Labels", "Machines", 
              "Paper", "Phones", "Storage", "Supplies", "Tables"]

    while (True):
        mode = input("\nWelcome to PerfectSalesman!\nDo you want to find the best product to go on sale for this month (a),\nor input a custom data point (b),\nor exit (q)?\n")
        if (mode == "q"):
            print("Thank you for participating!")
            break
        elif (mode == "a"):
            discountIncrement = 10
            result = find_best_profit_in_range(model, products, discount_range(discountIncrement))
            print(f"The best product to go in sale is: {result[0]} for {result[1]}%.")
            print(f"You will gain ${result[2][2]:.2f} in profit with {int(result[2][1])} Qty sold.")
        elif (mode == "b"):
            # User specified discount
            product = input("Please enter a product category: ")
            discount = input("Please enter discount percentage (format: dd%): ")
            discount = int(discount)
            # Error check: 
            if product not in products or discount > 100 or discount < 0: 
                print("Input Error, Please Try Again.")
            else:
                result = model(torch.Tensor([discount]+pd.get_dummies(pd.Series(products))[product].tolist()))
                print(f"You will gain ${result[2]:.2f} in profit with {int(result[1])} Qty sold.")
                #TODO: visualize graph
        else:
            print("Input Error, Please Try Again.")

demo()