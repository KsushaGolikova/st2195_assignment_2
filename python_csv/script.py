import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/Comma-separated_values"

# притворяемся обычным браузером
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()   # если сайт вернёт ошибку — увидим это явно

# читаем таблицы уже из HTML-текста
tables = pd.read_html(response.text)

cars = tables[0]  # первая таблица на странице

cars.to_csv("cars_from_wiki.csv", index=False)

