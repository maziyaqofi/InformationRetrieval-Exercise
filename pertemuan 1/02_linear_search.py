# MaziyaQofi
# Sep, 30 2026

# Kumpulan dokumen
documents = [
    "Machine learning untuk kesehatan",
    "Resep makanan Indonesia",
    "Artificial intelligence untuk diagnosis penyakit",
    "Machine learning untuk diagnosis penyakit",
    "Teknologi informasi dalam bidang kesehatan"
]


# Fungsi tokenisasi sederhana
def tokenize(text):
    return text.lower().split()


# Fungsi Linear Search
def linear_search(query, documents):
    results = []

    query_terms = tokenize(query)

    for doc in documents:
        score = 0

        doc_terms = tokenize(doc)

        for term in query_terms:
            if term in doc_terms:
                score = score + 1

        if score > 0:
            results.append((doc, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results


# Query pengguna
query = "machine learning kesehatan"


# Jalankan pencarian
results = linear_search(query, documents)


# Tampilkan hasil
print("Query:", query)
print("\nHasil pencarian:")

for doc, score in results:
    print(f"Score {score} | {doc}")