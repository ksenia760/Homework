my_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
     ]

my_lambda = lambda list_var: (list_var[3] + 10) \
    if list_var[3] < 100 else (list_var[3])
result = list(map(my_lambda, my_list))
print(result)


