import re

strings = ["abcde", "forever21", "george bush", "level 5", "twins2", "lululemon123t good"]

for s in strings:
    if re.search(r'\d+$', s):
        print(f"{s} has a match!")
    else:
        print(f"{s} not matched!")
