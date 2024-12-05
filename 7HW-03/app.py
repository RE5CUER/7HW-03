import requests
import sys

def download_favicon(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        favicon_url = url.rstrip("/") + "/favicon.ico"
        response = requests.get(favicon_url, stream=True)
        if response.status_code == 200:
            with open("favicon.ico", "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Favicon сохранён как favicon.ico")
        else:
            print(f"Не удалось найти favicon по адресу: {favicon_url}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите URL сайта в качестве аргумента.")
    else:
        download_favicon(sys.argv[1])
