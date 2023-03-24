import re

# define the pattern to match
pattern = r'\b\w*z\w*\b'

# define the sample text
text = "The quick brown fox jumps over the lazy dog. Python Exercises. I like pizza. UC Berkeley courses use Piazza"

# find all matches in the text
matches = re.findall(pattern, text)

# print the matches
for match in matches:
    print(match, "has a match!")
