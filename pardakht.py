from collections import Counter

def min_letters_to_buy(cls):
    for zolal_words in cls:
        max_counts = Counter()

        for word in zolal_words:
            word_count = Counter(word)

            for letter, count in word_count.items():
                max_counts[letter] = max(max_counts[letter], count)

        print(sum(max_counts.values()))

zol = int(input())
cls = []

for _ in range(zol):
    zoln = int(input())
    zolal_words = [input().strip() for _ in range(zoln)]
    cls.append(zolal_words)

min_letters_to_buy(cls)
