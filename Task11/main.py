##Assignment codes:-

#Nested Aggregation
def nested_aggregation(data):
    result = {}
    for dept, emp, sal in data:
        result.setdefault(dept, []).append((emp, sal))
    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)
    return result
 #inputs:-
data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]
nested_aggregation(data)

#Inverted Index
def inverted_index(sentences):
    index = {}
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            index.setdefault(word, []).append(i)
    return index
 #inputs:-
sentences = ["the cat climbed the tree", "birds chirped in the morning light", "a gentle breeze blew"
, "the sun set behind the mountains"]
inverted_index(sentences)

#Deep Copy Trap
import copy
original = {'a': [1, 2, 3]}
shallow = original.copy()
deep = copy.deepcopy(original)

shallow['a'].append(4)
print("Shallow Copy:", shallow, original)
original = {'a': [1, 2, 3]}
deep = copy.deepcopy(original)
deep['a'].append(4)
print("Deep Copy:", deep, original)

#Accumulate Word Lengths
def accumulate_word_lengths(words):
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result
words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
accumulate_word_lengths(words)

#Dictionary Merge with Conflict Resolution
def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] = max(result[key], value)
        else:
            result[key] = value
    return result
d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
merge_dicts(d1, d2)