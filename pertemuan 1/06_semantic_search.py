from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# 1. Load model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Kumpulan dokumen
documents = [
    "Sistem temu kembali informasi adalah bidang ilmu komputer",
    "Mobil listrik semakin populer di Indonesia",
    "Information retrieval focuses on finding relevant documents",
    "Pencarian semantik memahami makna di balik query",
]


# 3. Ubah dokumen menjadi embeddings
doc_embeddings = model.encode(
    documents,
    normalize_embeddings=True
)


# 4. Buat FAISS index
dim = doc_embeddings.shape[1]

index = faiss.IndexFlatIP(dim)

index.add(
    doc_embeddings.astype("float32")
)


# 5. Query
query = "cara mencari dokumen yang relevan"


# 6. Ubah query menjadi embedding
query_embedding = model.encode(
    [query],
    normalize_embeddings=True
)


# 7. Cari 3 dokumen paling mirip
scores, ids = index.search(
    query_embedding.astype("float32"),
    k=3
)


# 8. Tampilkan hasil
print("\nQuery:")
print(query)

print("\nHasil Semantic Search:")
print("=" * 60)

for score, doc_id in zip(scores[0], ids[0]):
    print(f"Score: {score:.4f}")
    print(f"Document: {documents[doc_id]}")
    print("-" * 60)