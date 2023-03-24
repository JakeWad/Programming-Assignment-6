import re

def find_sequences(s):
    pattern = r'[A-Z][a-z]*'
    if re.fullmatch(pattern, s):
        print(s + ' has a match!')
    else:
        print(s + ' not matched!')
        
find_sequences('AaBbGg')
find_sequences('Python')
find_sequences('python')
find_sequences('PYTHON')
find_sequences('aA')
find_sequences('Aa')
