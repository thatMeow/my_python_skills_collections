# https://stackoverflow.com/questions/31490101/create-a-dict-with-unique-keys-and-various-list-values-from-a-tuple
# Convert a list of tuples to a dict that has keys and values. If the keys have multiple values turn the values into a list

>>> aaa = list((('a', 1), ('b', 2), ('c', 3), ('a', 'zzz')))
>>> aaa
[('a', 1), ('b', 2), ('c', 3), ('a', 'zzz')]

>>> x = {}
>>> for tup in aaa:
>>>     x.setdefault(tup[0], []).append(tup[1])

{'a': [1, 'zzz'], 'b': [2], 'c': [3]}
