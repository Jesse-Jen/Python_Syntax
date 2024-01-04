def print_upper_words(words):
    '''Uppercases all characters'''
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])



def print_upper_words2(words):
    for word in words:
        if word[0] == 'e' or  word[0] == 'E':
            print(word.upper())

print_upper_words2(["ello", "ey", "goodbye", "yo", "Es"])



def print_upper_words3(words, letters):
    for word in words:
        if word[0].lower() in letters.lower():
            print(word.upper())


words = ["hello", "hey", "goodbye", "yo", "yes"]
letters = {'h', 'y'}
print_upper_words3(words, letters)