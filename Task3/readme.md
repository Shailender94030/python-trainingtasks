# Python Assignment

## Accessing Elements

### Access the Last Character of a String
```python
my_string = "Hello"
print(my_string[-1])  # Output: 'o'
```

### Access the Third Element of a List
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # Output: 30
```

### Length of a List with Nested Elements
```python
my_list = [1, [2, 3], 4]
print(len(my_list))  # Output: 3
```

## Slicing Operations

### Practical Example of Slicing
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
```

### Reverse a String Using Slicing
```python
my_string = "Hello"
print(my_string[::-1])  # Output: 'olleH'
```

## List Operations

### List Concatenation
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
```

### List Repetition
```python
list1 = [1, 2, 3]
result = list1 * 3
print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## List Methods

### Count Occurrences of an Element
```python
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3
```

### Difference Between `list.append()` and `list.extend()`
```python
lst = [1, 2]
lst.append(3)  # [1, 2, 3]
lst.extend([4, 5])  # [1, 2, 3, 4, 5]
```

## String Operations

### Split a Sentence into Words
```python
sentence = "Learn Python, step by step!"
words = sentence.split()
print(words)  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']
```

### Join a List into a String
```python
words = ['Python', 'is', 'fun']
result = ' '.join(words)
print(result)  # Output: 'Python is fun'
```

## Advanced List Operations

### Find Index of an Element
```python
numbers = [1, 2, 2, 3, 4, 2]
index = numbers.index(2)
print(index)  # Output: 1
```

### Check if a String is a Palindrome
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

### Find the Longest Word in a Sentence
```python
def longest_word(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(longest_word("The quick brown fox jumped"))  # Output: 6
```

## Nested Lists and Tuples

### Access Nested List Elements
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6
```

### Convert a List of Characters into a String
```python
char_list = ['h', 'e', 'l', 'l', 'o']
string = ''.join(char_list)
print(string)  # Output: 'hello'
```

### Remove Duplicates While Preserving Order
```python
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 4]))
```

## Sorting and Flattening Lists

### Sort a List of Tuples by Second Element
```python
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 1), (4, 2)]))  # Output: [(2, 1), (4, 2), (1, 3)]
```

### Flatten a Nested List
```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

## Special String and List Operations

### Rotate a List Right by k Steps
```python
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
```

### Check if Two Strings are Anagrams
```python
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # Output: True
```

### Split a List into Chunks
```python
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4, 5, 6], 2))  # Output: [[1, 2], [3, 4], [5, 6]]
```

### Merge Two Sorted Lists
```python
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```


