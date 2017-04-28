import itertools

for _ in itertools.repeat(None, N):
    do_something()
    
    
# e.g. pick a random letter from a string then insert into a list

string = 'abc'
import itertools
list_ = []
for _ in itertools.repeat(None, 10):
    list_.append(random.choice(string))
    
list_
