from data_sandbox import get_random_search_queries


class QueryClass:
    def __init__(self):
        self.queries = get_random_search_queries()
        self.my_dict = {}

    def get_queries(self):
        for query in self.queries:
            self.my_dict[query] = self.my_dict.get(query, 0) + 1

    def get_dict(self):
        for query, count in self.my_dict.items():
            print(f"Запрос: ({query}) - {count} шт.")


if __name__ == '__main__':
    query_class = QueryClass()
    query_class.get_queries()
    query_class.get_dict()
