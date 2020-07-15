# The following variables will be provided by the grading environment, you can
# access them without declaration. However, you can freely adopt the following
# values to play around with the script, as long as you keep them in the "if".
if __name__ == "__main__":
    price_cone = 0.5
    price_per_scoop_vanilla = 2
    price_per_scoop_chocolate = 1.10

    num_scoops_vanilla = 1
    num_scoops_chocolate = 3

# calculate the total price of such an order, do not forget the cone!
price = price_cone + (price_per_scoop_chocolate * num_scoops_chocolate) + (price_per_scoop_vanilla * num_scoops_vanilla)
