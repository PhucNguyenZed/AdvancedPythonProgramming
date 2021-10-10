def count_values(dictionary):
    return len(set(dictionary.values()))
print(count_values({'red': 1, 'green': 2, 'blue': 2}))