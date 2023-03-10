words = "happy, funny, sad, funny, beautiful"
list_words = words.split()
print(list_words)
set_words = set(list_words)
print(set_words)
new_dict = {}
for word in set_words:
    new_dict[word] = words.count(word)
    print(new_dict)