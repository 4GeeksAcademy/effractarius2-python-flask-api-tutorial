from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "label": "My first task", "done": False},
    {"id": 2, "label": "My second task", "done": False},
    {"id": 3, "label": "My third task", "done": False}
]



@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    new_id = len(todos) + 1
    new_todo = {
        "id": new_id,
        "label": request_body.get("label"),
        "done": request_body.get("done", False)
    }

    todos.append(new_todo)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Invalid position"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)