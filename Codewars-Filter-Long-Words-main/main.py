"""
Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

Example:

filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']
"""

def filter_long_words(sentence, n):
    matched = []
    all_words = sentence.split()
    for i in all_words:
        if len(i) > n:
            matched.append(i)

    return print(matched)


filter_long_words("The quick brown fox jumps over the lazy dog", 2)
