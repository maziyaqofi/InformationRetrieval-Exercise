# MaziyaQofi
# Sep, 30 2026

from collections import Counter

# Make a document
documents = [
    "machine learning untuk kesehatan",
    "machine learning untuk diagnosis penyakit",
    "teknologi informasi untuk kesehatan",
    "machine learning machine untuk prediksi"
    "kesehatan pada mahasiswa"
    "teknologi kesehatan yang sedang dikembangkan"
    "Penyakit yang sering terjadi pada kesehatan manusia"
]

# token
def tokenize(text):
    return text.lower().split()

def build_inverted_index(documents):

    index = {}

    for doc_id, doc in enumerate(documents):

        terms = tokenize(doc)

        term_freq = Counter(terms)

        for term, freq in term_freq.items():

            if term not in index:
                index[term] = []

            index[term].append((doc_id, freq))

    return index


index = build_inverted_index(documents)


print("=== INVERTED INDEX ===")

for term, postings in index.items():
    print(term, "->", postings)

