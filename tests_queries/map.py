import requests

url = "http://127.0.0.1:5000/perform_query"

payload = {
  "file_name": "apache_logs.txt",
  "cmd1": "map",
  "value1": "0"  # или любой другой номер колонки
}


response = requests.post(url, json=payload)
print(response.text)
