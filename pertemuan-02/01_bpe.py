# MaziyaQofi
# 7, Oct 2026

# impor modul collections untuk mengambil kelas Counter
from collections import Counter 

def get_pairs(tokens):
    pairs = Counter()

    for word in tokens:
        for i in range(len(word) - 1):
            pair = (word[i], word[i + 1])
            pairs[pair] += 1

    return pairs


def merge_pair(tokens, pair):
    new_tokens = []

    for word in tokens:
        new_word = []
        i = 0

        while i < len(word):
            if (
                i < len(word) - 1
                and word[i] == pair[0]
                and word[i + 1] == pair[1]
            ):
                new_word.append(word[i] + word[i + 1])
                i += 2
            else:
                new_word.append(word[i])
                i += 1

        new_tokens.append(new_word)

    return new_tokens


def bpe_train(corpus, num_merges):

    # Split setiap kata menjadi karakter
    tokens = [list(word) for word in corpus]

    # Vocabulary awal
    vocab = set()

    for word in tokens:
        vocab.update(word)

    merge_rules = []

    print("Token awal:")
    print(tokens)

    for step in range(num_merges):

        pairs = get_pairs(tokens)

        if not pairs:
            break

        # Cari pasangan paling sering
        best = pairs.most_common(1)[0][0]

        # Simpan aturan
        merge_rules.append(best)

        # Gabungkan pasangan
        new_token = best[0] + best[1]
        vocab.add(new_token)

        tokens = merge_pair(tokens, best)

        print(f"\nMerge {step + 1}: {best} -> {new_token}")
        print(tokens)

    return vocab, merge_rules

def bpe_tokenize(word, rules):

    # Pecah kata menjadi karakter
    tokens = list(word)

    # Terapkan setiap merge rule
    for pair in rules:
        new_tokens = []
        i = 0

        while i < len(tokens):

            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_tokens.append(tokens[i] + tokens[i + 1])
                i += 2

            else:
                new_tokens.append(tokens[i])
                i += 1

        tokens = new_tokens

    return tokens

def bpe_tokenize(word, rules):
    tokens = list(word)

    for pair in rules:
        new_tokens = []
        i = 0

        while i < len(tokens):
            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_tokens.append(tokens[i] + tokens[i + 1])
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1

        tokens = new_tokens

    return tokens

# Corpus sederhana
corpus = ["low", "lower", "lowest"]

vocab, rules = bpe_train(corpus, num_merges=5)

print("\nVocabulary:")
print(vocab)

print("\nMerge Rules:")
print(rules)

word = "lowest"

result = bpe_tokenize(word, rules)

print("\nBPE Tokenization:")
print("Word:", word)
print("Tokens:", result)