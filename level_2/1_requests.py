"""
- хттп(с)
- методы
- тело запроса
- квери параметры
- урл параметры
- заголовки
- куки
- API
- REST API
- статус код
"""
import requests
from pprint import pprint
import test_module
from requests.exceptions import ConnectionError, ConnectTimeout

# обработка ошибок
# таймаут


def get_html():
    # пример гет запроса html
    response = requests.get("https://yandex.ru/search/?clid=9582&text=dfgfdg&l10n=ru&lr=10752")
    print(response.status_code)
    print(response.text)


def get_json():
    # пример гет запроса json
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    pprint(data)
    print(type(data))


def post():
    # Пример пост запроса
    # Передача заголовков
    # Передача куков
    url = "https://jsonplaceholder.typicode.com/users"
    data = {
        "name": "Dmitry",
        "username": "fat_sana"
    }
    headers = {"Custom": "Custom"}
    cookies = {"Custom": "Custom"}
    response = requests.post(url, json=data, headers=headers, cookies=cookies)
    print(response)
    print(response.headers)
    print(response.cookies)
    print(response.text)


def error_request():
    url = "https://ffdfsdfsdf.rom"
    try:
        response = requests.get(url, timeout=3)
    except (ConnectionError, ConnectTimeout):
        print(f"УПС, сервер не отвечает: {url}")


# сессия
def session():
    session = requests.Session()
    session.headers.update({"User-Agent": "my-app"})
    # Первый запрос
    response1 = session.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
    print("Установленные куки:", session.cookies)
    # Второй запрос
    response2 = session.get("https://httpbin.org/cookies")
    print("Ответ с куки:", response2.json())


if __name__ == "__main__":
    # print(__name__)
    # print(test_module.__name__)
    # get_html()
    # get_json()
    # post()
    error_request()
    # session()
