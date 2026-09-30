# MaziyaQofi
# Sep, 30 2026

import re
from collections import Counter, defaultdict


class SimpleIR:

    def __init__(self):
        self.documents = {}
        self.inv_index = defaultdict(list)

    def add_document(self, doc_id, text):
        """Tambah dokumen ke koleksi"""

        self.documents[doc_id] = text

        terms = self.tokenize(text)
        freq = Counter(terms)

        for term, f in freq.items():
            self.inv_index[term].append((doc_id, f))

    def tokenize(self, text):
        """Tokenisasi sederhana: lowercase + split"""

        return re.findall(r'\w+', text.lower())

    def search(self, query, top_k=5):
        """Pencarian dengan term frequency scoring"""

        query_terms = self.tokenize(query)

        scores = Counter()

        for term in query_terms:
            for doc_id, freq in self.inv_index.get(term, []):
                scores[doc_id] += freq

        return scores.most_common(top_k)


# ==========================
# DEMO
# ==========================

ir = SimpleIR()


docs = [
    "Sistem temu kembali informasi adalah bidang ilmu komputer",
    "Information retrieval berfokus pada pencarian dokumen",
    "Machine learning digunakan untuk klasifikasi teks",
    "Search engine menggunakan inverted index untuk pencarian",
    "Natural language processing membantu pemahaman teks",
]


for i, doc in enumerate(docs):
    ir.add_document(f"D{i+1}", doc)


query = "cara mencari dokumen yang relevan"

results = ir.search(query)


print("Query:", query)
print("=" * 60)

for doc_id, score in results:
    print(f"{doc_id}: score={score} | {ir.documents[doc_id]}")