## Assignment
# Access the last character of a string
my_string = "Hello"
print(my_string[-1]) 
#O/P:- Last character= 'o'

#Create a list and access third element
my_list = [10, 20, 30, 40, 50]
print(my_list[2]) 
#O/P:- 30 

#Result of len([1, [2, 3], 4])
my_list = [1, [2, 3], 4]
print(len(my_list))  
#O/P:- 3

#Slicing with a practical example
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  
#O/P:- [20, 30, 40]

#Reverse a string using slicing
my_string = "Hello"
print(my_string[::-1])  ]
#O/P:- olleH'

#List Concatenation
#Concatenation combines two or more lists  in 1 iteam
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  
#O/P:-[1, 2, 3, 4, 5, 6]
#List Repetition
#Repetition repeats a list multiple times
list1 = [1, 2, 3]
result = list1 * 3
print(result)  
#O/P:- [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Count Occurrences of an Element in a List
#Use the count() method for it
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(count)  
#O/P:- 3

#Output:- my_tuple = (1, 2, 3); print(my_tuple[1:])
my_tuple = (1, 2, 3)
print(my_tuple[1:])  
#O/P:- (2, 3)

#Difference between list.append() and list.extend()
#list.append(): Adds a single element to the end of the list.
#list.extend(): Adds all elements from another iterable (like a list) to the end of the list
#Example:
lst = [1, 2]
lst.append(3)  
#O/P:- [1, 2, 3]
lst.extend([4, 5])  
#O/P:- [1, 2, 3, 4, 5]

#Code to split the sentence "Learn Python, step by step!" into words
sentence = "Learn Python, step by step!"
words = sentence.split()
print(words)  
#O/P:-: ['Learn', 'Python,', 'step', 'by', 'step!']

#Join a list ['Python', 'is', 'fun'] into a single string:
words = ['Python', 'is', 'fun']
result = ' '.join(words)
print(result)  
#O/P:- 'Python is fun'

#Find the index of the first 2 in the list numbers = [1, 2, 2, 3, 4, 2]
numbers = [1, 2, 2, 3, 4, 2]
index = numbers.index(2)
print(index)  
#O/P:- 1

#Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  
#O/P:- True
print(is_palindrome("hello"))    
#O/P:- False

#Find the length of the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(longest_word("The quick brown fox jumped"))  
#O/P:-6

#Nested list indexing
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # 6

#Convert a list of characters into a string
char_list = ['h', 'e', 'l', 'l', 'o']
string = ''.join(char_list)
print(string)  
#O/P:- "hello"

#Remove duplicates from a list while preserving order
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 4]))  

#Sort a list of tuples by the second element of each tuple
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 1), (4, 2)]))  
#O/P:- [(2, 1), (4, 2), (1, 3)]

#Flatten a nested list of arbitrary depth
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1, [2, [3, 4], 5], 6]))  
#O/P:- [1, 2, 3, 4, 5, 6]

#Rotate a list to the right by k steps
def rotate_list(lst, k):
    k = k % len(lst)  
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  
#O/P:- [4, 5, 1, 2, 3]

#Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))  #

#Split a list into chunks of a specified size
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]
  
print(chunk_list([1, 2, 3, 4, 5, 6], 2))  
#O/P:- [[1, 2], [3, 4], [5, 6]]

#Merge two sorted lists into one sorted list
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
#O/P:- [1, 2, 3, 4, 5, 6]

####Sequences Questions:-

#Identify the longest pipeline and return pipelines taking more than a given threshold time
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40
#Identify the longest pipeline
longest_pipeline = max(pipelines, key=lambda x: x[1])
#Find pipelines exceeding the threshold
exceeding_threshold = [pipeline[0] for pipeline in pipelines if pipeline[1] > threshold]
print(f"Longest Pipeline: {longest_pipeline[0]}")
print(f"Pipelines exceeding threshold: {exceeding_threshold}")


#Extract unique error codes from a log file
import re
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""
#Extract error codes using regex
error_codes = set(re.findall(r'ERROR (\d+)', logs))
print("Unique Error Codes:", error_codes)

#Parse key-value pairs from a configuration string
config = "host=127.0.0.1;port=8080;mode=debug"
#Parse the config string into key-value pairs
config_dict = [tuple(item.split('=')) for item in config.split(';')]
print(config_dict)

#Extract unique hashtags from a social media post
import re
post = "Loving the new #Python course! #Coding #Python #Learning"
#Extract unique hashtags using regex
hashtags = list(set(re.findall(r'#\w+', post)))
print(hashtags)

#Extract every third character from a string
secret_message = "hweollrolwd"
#Extract every third character starting from index 0
result = secret_message[::3]
print(result)

#Find the product with the highest quantity
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]
#Find the product with the highest quantity
max_product = max(inventory, key=lambda x: x[1])
print(max_product[0])

#Extract scores from a survey string and find min/max
survey_data = "5,3,4,1,2"
#Convert the survey data to a list of integers
scores = list(map(int, survey_data.split(',')))
#Find the min and max scores
max_score = max(scores)
min_score = min(scores)
print(f"Max Score: {max_score}, Min Score: {min_score}")

#Manage user access levels using lists and tuples
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")
#Zip users and roles together and print the result
user_roles = zip(users, roles)
#Format and print each user with their role
for user, role in user_roles:
    print(f"{user}: {role}")

#Categorize tickets based on message length
message = "My account is locked, please help!"
#Categorize based on message length
length = len(message)
if length < 30:
    category = "Short"
elif 30 <= length <= 60:
    category = "Medium"
else:
    category = "Long"
print(f"Category: {category}")

#Find the product with the longest name
products = ["Laptop", "Smartphone", "Wireless Headphones"]
#Find the product with the longest name
longest_product = max(products, key=len)
print(longest_product)

#Extract the last 10 sensor readings and calculate the average
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
#Extract the last 10 readings
last_10_readings = sensor_readings[-10:]
#Calculate the average
average = sum(last_10_readings) / len(last_10_readings)
print(f"Average: {average}")

#Reverse the list of transactions
transactions = [100, -50, 200, -150, 50]
#Reverse the list
reversed_transactions = transactions[::-1]
print(reversed_transactions)

#Format logs with timestamps.
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"
#Format each log with the timestamp
formatted_logs = [f"{timestamp}: {log}" for log in logs]
print(formatted_logs)

#Generate patterns with repetition
symbol = "*"
count = 5
#Generate the pattern
pattern = ' '.join([symbol] * count)
print(pattern)

#Count keyword occurrences
feedback = "The product is excellent, absolutely excellent!"
keyword = "excellent"
#Count the occurrences of the keyword
count = feedback.lower().split().count(keyword.lower())
print(f"'{keyword}' count: {count}")

#Find the index of the first occurrence of "error"
log = "INFO: All systems go. ERROR: Failed to start service."
#Find the index of the first occurrence of "ERROR"
index = log.find("ERROR")
print(f"Index: {index}")

#Parse CSV data into lists
csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
#Parse CSV data into lists
parsed_data = [line.split(',') for line in csv_data.split('\n')]
print(parsed_data)

#Generate usernames from full names
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
#Generate usernames
usernames = [name.split()[0][0] + name.split()[1] for name in names]
print(usernames)

#Count messages per user from chat logs
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]
#Count messages per user
message_count = {}
for log in chat_logs:
    user = log.split(':')[0]
    message_count[user] = message_count.get(user, 0) + 1
#Print the message count for each user
for user, count in message_count.items():
    print(f"{user}: {count} messages")

#Compress recurring substrings
data = "abababababab"
substring = "ab"
count = len(data) // len(substring)
print(f"'{substring}' repeated {count} times")
