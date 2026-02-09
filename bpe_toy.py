from collections import Counter

# ---------- Toy corpus for Q2.2 ----------
corpus = [
"low_", "low_", "low_", "low_", "low_",
"lowest_", "lowest_",
"newer_", "newer_", "newer_", "newer_", "newer_", "newer_",
"wider_", "wider_", "wider_",
"new_", "new_"
]

def split_words(words):
    return [list(word) for word in words]

tokens = split_words(corpus)

def get_bigrams(words):
    pairs = []
    for word in words:
        for i in range(len(word)-1):
            pairs.append((word[i], word[i+1]))
    return Counter(pairs)

def merge_pair(words, best_pair):
    new_words = []
    a, b = best_pair
    for word in words:
        new_word = []
        i = 0
        while i < len(word)-1:
            if word[i] == a and word[i+1] == b:
                new_word.append(a+b)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        if i == len(word)-1:
            new_word.append(word[i])
        new_words.append(new_word)
    return new_words

print("Initial vocab size:", len(set(sum(tokens, []))))

for step in range(10):
    bigrams = get_bigrams(tokens)
    best_pair = bigrams.most_common(1)[0][0]
    tokens = merge_pair(tokens, best_pair)
    vocab = set(sum(tokens, []))
    print(f"Step {step+1}: merging {best_pair} -> vocab size = {len(vocab)}")
