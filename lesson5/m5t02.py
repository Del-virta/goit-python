articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_list = []
    for article in articles_dict:
        if article['title'].find(key) !=-1 or article['author'].find(key) !=-1:
            new_list.append(article)
    return new_list 