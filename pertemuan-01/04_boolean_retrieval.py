# MaziyaQofi
# Sep, 30 2026

# Inverted Index sederhana

index = {
    "machine": {0, 1, 3},
    "learning": {0, 1, 3},
    "kesehatan": {0, 2},
    "diagnosis": {1},
    "teknologi": {2}
}


def boolean_search(query, index):

    # Pecah query
    parts = query.lower().split()

    # Contoh:
    # "machine AND kesehatan"
    #
    # menjadi:
    # ["machine", "and", "kesehatan"]

    term1 = parts[0]
    operator = parts[1]
    term2 = parts[2]

    # Ambil dokumen untuk masing-masing term
    docs1 = index.get(term1, set())
    docs2 = index.get(term2, set())

    # Boolean AND
    if operator == "and":
        result = docs1.intersection(docs2)

    # Boolean OR
    elif operator == "or":
        result = docs1.union(docs2)

    else:
        result = set()

    return result


query = "diagnosis AND machine"

hasil = boolean_search(query, index)

print("Query :", query)
print("Hasil :", hasil)