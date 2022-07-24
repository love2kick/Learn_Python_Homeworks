from collections import Counter

def most_common_words(filepath, number_of_words=3):
    x=open(filepath, "r", encoding='utf-8').read()
    words=[i.lower().replace(",","").replace(".","") for i in x.split()]
    most_occurs=Counter(sorted(words)).most_common(number_of_words)
    occwordlist=[i[0] for i in most_occurs]
    return occwordlist

print(most_common_words('./data/lorem_ipsum.txt'))