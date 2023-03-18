import requests

url = "http://127.0.0.1:5000/perform_query"

payload = {
  "file_name": "apache_logs.txt",
  "cmd1": "sort",
  "value1": "asc",
  "cmd2": "limit",
  "value2": "1"
}

response = requests.post(url, json=payload)
print(response.text)
