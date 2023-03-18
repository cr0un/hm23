from flask import Flask, request, jsonify
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route('/perform_query', methods=['POST'])
def perform_query():
    # Получение параметров из запроса
    payload = request.get_json(force=True)
    cmd1 = payload.get("cmd1")
    value1 = payload.get("value1")
    cmd2 = payload.get("cmd2")
    value2 = payload.get("value2")
    file_name = payload.get("file_name")

    # проверка полученных параметров
    print(f"Received parameters: cmd1={cmd1}, value1={value1}, cmd2={cmd2}, value2={value2}, filename={file_name}")

    data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

    # Открытие файла из папки data
    try:
        with open(os.path.join(data_folder, file_name), 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        return jsonify({"error": f"File '{file_name}' not found in the data folder"}), 404


    # Обработка файла согласно командам
    if cmd1 == 'filter':
        content = filter(lambda x: value1 in x, content)
    elif cmd1 == 'map':
        col = int(value1)
        content = map(lambda x: x.split()[col], content)

    if cmd2 == 'unique':
        content = list(set(content))
    elif cmd2 == 'sort':
        content = sorted(content, reverse=value2 == 'desc')
    elif cmd2 == 'limit':
        limit = int(value2)
        content = content[:limit]

    # Возвращение результата клиенту
    result = "\n".join(content)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)

