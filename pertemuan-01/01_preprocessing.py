# MaziyaQofi
# Sep, 30 2026
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "Sistem Temu Kembali Informasi"

tokens = word_tokenize(text)

print("Kalimat asli:")
print(text)

print("\nHasil tokenisasi:")
print(tokens)