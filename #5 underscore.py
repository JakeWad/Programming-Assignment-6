def replace_spaces(text):
    text_with_underscore = text.replace(' ', '_')
    text_with_space = text.replace('_', ' ')
    print(f"Original String:  {text}")
    print(f"space by _     :  {text_with_underscore}")
    print(f"_ by space     :  {text_with_space}")
    print("\n")
    
replace_spaces("Wall Street")
replace_spaces("Computer Science")
replace_spaces("long long ago")
replace_spaces("real-estate")
