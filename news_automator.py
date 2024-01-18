import requests

API_KEY= "51680cfbcf254801bbaaab62c402de54"

URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "br",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    total_results = response.json()['totalResults']

    print(total_results)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article['title'], "url": article['url']})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')


category_input = input("Type one of this category (business, entertainment, general, health, science, sports, technology): ")

get_articles(category_input)


