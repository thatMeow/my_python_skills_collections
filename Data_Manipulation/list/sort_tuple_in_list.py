# Sort a list of tuples by 2nd item (integer value)

# https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])
