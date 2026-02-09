from collections import Counter
import re

text = """
I love natural language processing.
It helps machines understand human language.
Many researchers study neural networks.
Modern transformers power chatbots like ChatGPT.
NLP is everywhere in technology today.
"""

words = re.findall(r"[A-Za-z]+", text.lower())
corpus = [w + "_" for w in words]

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

merges = []

for step in range(30):
    bigrams = get_bigrams(tokens)
    best_pair = bigrams.most_common(1)[0][0]
    merges.append(best_pair)
    tokens = merge_pair(tokens, best_pair)

print("Top 5 merges:", merges[:5])
vocab = set(sum(tokens, []))
longest = sorted(vocab, key=len, reverse=True)[:5]
print("Longest tokens:", longest)
