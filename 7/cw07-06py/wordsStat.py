import re

text = "Hello my Friend it's me alesha - your best friend"
splitted_words = re.split(r"[.,:;!?\-&]+", text)
words = map(lambda word: word.lower(), splitted_words)
words_stats = {}

for word in words:
    words_stats[word] = words_stats.get(word, 0) + 1
    
stats = list(words_stats.items())
stats.sort(reverse=True, key=lambda stat: stat[1])
print(*stats, sep="\n")