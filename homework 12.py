words = "happy, funny, sad, funny, beautiful"
list_words = words.split()
new_dict = {}
for word in list_words:
    new_dict[word] = words.count(word)
    print(new_dict)
