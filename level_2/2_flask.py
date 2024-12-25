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
https://flask.palletsprojects.com/en/stable/quickstart/
"""

from flask import Flask, jsonify, abort, request, make_response


app = Flask(__name__)


database = [
    {
        "name": "Diman",
        "age": 33
    },
    {
        "name": "Kolan",
        "age": 23
    }
]


# обработчик / хендлер / ручка / эндпоинт - вьюха / представление
@app.route("/url123")
def hello_world():
    return "<h1>ЗДАРОВА ДИМАН!!!</h1><p>Hello, World!</p>"


# CRUD
@app.route("/users", methods=['GET', 'POST'])
@app.route("/users/<int:idx>", methods=['GET', 'PATCH', "DELETE"])
def users(idx=None):
    headers = request.headers
    print(dict(headers))
    if dict(headers).get("Super-Admin") == "TRUE":
        print("АДМИН ПРИШЕЛ НА СЕРВЕР!!!")
    else:
        abort(404, description="ПОШЕЛ ВОН!!!")

    if request.method == "GET":
        # READ
        if idx is not None:
            if idx >= len(database):
                abort(404, description=f"User with id {idx} not found")
            return jsonify(database[idx])
        return jsonify(database)
    if request.method == "POST":
        # CREATE
        user_data = request.json
        database.append(user_data)
        user_data.update({"id": len(database)})
        return jsonify(user_data)
    if request.method == "PATCH":
        # UPDATE
        user_data = request.json
        age = user_data["age"]
        database[idx]["age"] = age
        return jsonify(database[idx])
    if request.method == "DELETE":
        user = database.pop(idx)
        print({"message": f"Пользователь {user['name']} удален!"})
        return make_response(
            "",
            204
        )  # 204 No Content


if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')
