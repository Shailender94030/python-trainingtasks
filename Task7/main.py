
#Codes:-

# For Loop Basics: Write a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# String Iteration: Write a program that counts vowels in a string.
def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
            return count
        
# Accumulator Pattern: Calculate the sum of squares from 1 to 100.
sum = 0
for i in range(1, 101):
    sum += i ** 2
    print(sum)

# Nested Loops: Create a multiplication table up to 10x10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')

# Image Processing: Use PIL to invert the colors of an image.
from PIL import Image
img = Image.open('image.jpg') # Opening img.
img = img.point(lambda x: 255 - x) #changing color here.
img.save('result_image.jpg') # saving result img.
