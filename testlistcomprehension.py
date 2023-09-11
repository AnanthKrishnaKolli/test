def generate_fruit_basket(fruits):
    """Without list comprehension"""
    basket = []
    for fruit in fruits:
        if fruit != "grapes":
            basket.append(fruit)
    return basket

print(generate_fruit_basket(['apples','grapes','bananas','watermelons']))