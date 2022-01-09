from PerfectSalesman.python.interface.utils import discount_range
from PerfectSalesman.python.interface.utils import find_best_profit_in_range
from model.Model import Model

def select_mode(mode="Best"):
    # TODO: get current month and decide path
    modelPath = '/content/december.pt'
    model = Model()
    model.load_state_dict(torch.load(modelPath, map_location=torch.device('cpu')))

    if mode == "Best":
        discountIncrement = 20
        products = ["Accessories", "Appliances", "Art", "Binders", "Bookcases", "Chairs", 
              "Copiers", "Envelopes", "Fasteners", "Furnishings", "Labels", "Machines", 
              "Paper", "Phones", "Storage", "Supplies", "Tables"]
        find_best_profit_in_range(model, products, discount_range(discountIncrement))
    else:
        # ? User specified discount
        discount = input("Please enter discount percentage (format: dd%)")

    pass
