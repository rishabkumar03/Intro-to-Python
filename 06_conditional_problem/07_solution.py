# COFFEE CUSTOMIZATION
    # Customize a coffee order: "Small", "Medium", or "Large" with an option for 'Extra shot' of espresso.

order_size = "Small"
extra_shot = False

if extra_shot == True:
    print(order_size, "size coffee is enriched with extra shot of espresso.")
else:
    print(order_size, "size coffee")