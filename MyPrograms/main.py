from data_sandbox import get_random_search_queries

# Получаем список запросов
queries = get_random_search_queries()

# Создаем словарь для подсчета
query_counts = {}

# Подсчитываем количество каждого запроса
for query in queries:
    query_counts[query] = query_counts.get(query, 0) + 1

# Выводим результаты (необязательно для проверки)
for query, count in query_counts.items():
    print(f"Запрос '{query}' встречается {count} раз(а)")