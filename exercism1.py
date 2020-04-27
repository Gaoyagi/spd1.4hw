# Given a word, compute the scrabble score for that word.

#questions:
# is it case sensitive

#assumptions:
#isnt case sensitive

def scrabble_score(word):
    scores = {
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 5,
        'g': 2,
        'h': 5,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 5,
        'w': 5,
        'x': 8,
        'y': 5,
        'z': 10
    }
    score = 0
    for letter in word:
        l = letter.lower()
        if scores.get(l) == None:
            return None            
        score+=scores[l]
    return score

assert scrabble_score("cabbage") == 14
assert scrabble_score("Cabbage") == 14
assert scrabble_score("ca4bage") == None

