import re

pattern = r'a+b*'

strings = ['ac', 'abc', 'abbc', 'eieio ax zzbb cc a bba', 'aaaabab aaa', 'xxxx abzzzzz', 'uuuuuu']

for string in strings:
    if re.search(pattern, string):
        print(string, 'has a match!')
    else:
        print(string, 'not matched!')
