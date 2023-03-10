d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}
new_dict = dict((val, key) for (key, val) in d.items())
print(new_dict)