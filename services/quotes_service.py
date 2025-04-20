import requests


def get_inspirational_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    quote_data = response.json()[0]
    author = quote_data["a"]
    quote = quote_data["q"]

    return f"{quote} - {author}"
