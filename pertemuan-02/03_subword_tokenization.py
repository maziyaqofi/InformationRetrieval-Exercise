# MaziyaQofi
# 7, Oct 2026

from transformers import AutoTokenizer

# WordPiece (BERT)
tok_bert = AutoTokenizer.from_pretrained("bert-base-uncased")

print(
    "WordPiece:",
    tok_bert.tokenize("unhappiness is unplayable")
)


# BPE (GPT-2)
tok_gpt = AutoTokenizer.from_pretrained("gpt2")

print(
    "BPE:",
    tok_gpt.tokenize("unhappiness is unplayable")
)


# IndoBERT (Bahasa Indonesia)
tok_indo = AutoTokenizer.from_pretrained(
    "indobenchmark/indobert-base-p1"
)

print(
    "IndoBERT:",
    tok_indo.tokenize("mahasiswa mempelajari pembelajaran mesin")
)


# Vocabulary Size
print(f"BERT vocab: {tok_bert.vocab_size}")
print(f"GPT2 vocab: {tok_gpt.vocab_size}")
print(f"IndoBERT vocab: {tok_indo.vocab_size}")