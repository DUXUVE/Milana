words = ['hello', 'memorize', 'hi', 'google']

VOWELS = 'euioa'

def count_vowels(text: str):
    count = 0
    for letter in text:
        if letter in VOWELS:
            count += 1
    return count

def take_consonants(text: str):
    for letter in text:
        if letter not in VOWELS:
            yield letter

for word in words:
    if count_vowels(word) > 2:
        print(''.join (take_consonants(word)))