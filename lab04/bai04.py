def get_authors(filenames):
    authors = set()
    for filename in filenames:
        pdb_file = open(filename)
    for line in pdb_file:
        if line.lower().startswith('author'):
            author = line[6:].strip()
            authors.add(author)
    return authors
print(get_authors)