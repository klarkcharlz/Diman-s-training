import threading
import requests


def fetch_url(url):
    print(f"Начинаем загрузку: {url}")
    response = requests.get(url)
    print(f"Загрузка завершена: {url}, символов: {len(response.text)}")


def main():
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.yandex.ru"
    ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Все загрузки завершены.")


if __name__ == "__main__":
    main()
