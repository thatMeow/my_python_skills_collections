import itertools

for _ in itertools.repeat(None, N):
    do_something()

# e.g. pick a random letter from a string then insert into a list
# "_" is just a random character here

string = 'abc'
import itertools
list_ = []
for _ in itertools.repeat(None, 10):
    list_.append(random.choice(string))
    
list_

#result:
['c', 'a', 'b', 'c', 'c', 'a', 'b', 'b', 'c', 'a']
