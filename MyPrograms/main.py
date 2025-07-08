
# Списковое включение_________________________________________________________________
from data_sandbox import get_random_search_queries

queries = get_random_search_queries()
my_dict = {}

my_dict_two = [i for i in queries if my_dict.setdefault(i, queries.count(i))]
print(my_dict)

# Списковое включение_________________________________________________________________

from data_sandbox import get_random_search_queries

queries = get_random_search_queries()  
my_dict = {}

my_dict_two = [i for i in queries if i not in my_dict.keys() and my_dict.setdefault(i, queries.count(i))]
print(my_dict)
