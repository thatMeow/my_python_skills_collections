string = "sdasdsadsaeio"
vowel_pos = [ i for i,v in enumerate(string) if v.lower() in ('aeiou') ]
vowel_pos

# result:
[2, 6, 9, 10, 11, 12]

