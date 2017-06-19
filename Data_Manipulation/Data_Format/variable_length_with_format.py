'''

Use {:<n} to spacify the length from the format() method.

'''


>>> for (tag, guess, name) in sorted(errors):
...     print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))
