def count_duplicates(dictionary):
        duplicates = 0
        values = list(dictionary.values())
        for item in values:
            if values.count(item) >= 2:
                duplicates = duplicates + 1
                num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)
        return duplicates
print(count_duplicates({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3}))