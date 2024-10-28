# Sample text input
text = """In a world full of ideas, we often find that ideas can be both inspiring and overwhelming.
Ideas can change the way we think, live, and interact with each other."""

# Convert text to lowercase and remove punctuation
text = text.lower()
for char in ',.':
    text = text.replace(char, '')

# Split the text into words
words = text.split()

# Initialize an empty dictionary to store word frequency
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word frequency dictionary
print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
