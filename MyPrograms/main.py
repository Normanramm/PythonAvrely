from data_sandbox import get_random_search_queries


queries = get_random_search_queries()
my_dict = {}

for query in queries:
    my_dict[query] = my_dict.get(query, 0) + 1

for query, count in my_dict.items():
    print(f"Запрос: ({query}) - {count} шт.")