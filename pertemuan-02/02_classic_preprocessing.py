# MaziyaQofi
# 7, Oct 2026

import re
import nltk

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Membuat stemmer Bahasa Indonesia
stemmer = StemmerFactory().create_stemmer()

# Mengambil daftar stopword Bahasa Indonesia
stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.get_stop_words()


def preprocess(text):

    # 1. Case Folding
    text = text.lower()

    # 2. Remove Special Characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 3. Tokenisasi
    tokens = nltk.word_tokenize(text)

    # 4. Stopword Removal
    tokens = [t for t in tokens if t not in stopwords]

    # 5. Stemming
    tokens = [stemmer.stem(t) for t in tokens]

    return tokens


text = "Pembelajaran mesin digunakan untuk klasifikasi dokumen"

print(preprocess(text))