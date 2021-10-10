def is_balanced(color_to_factor):
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0
print(is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7}))