import os
import re

# Display current working directory
print("Current working directory:", os.getcwd())

# Step 1: Read the file content
file_path = "c:\\Users\\chobodi\\Desktop\\Staff Research\\VCS Research\\Test Project\\data.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Step 2: Extract words using regex
words = re.findall(r'\b\w+\b', content)

# Step 3: Sort words alphabetically (case-insensitive)
words_sorted = sorted(words, key=str.lower)

# Step 4: Print sorted words
print("Extracted words:")
for word in words_sorted:
    print(word)

