from flask import Flask 
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message" : "Welcome to the Todo API"
    })

todos = [
    {"id": 1, "task": "Learn Python"},
    {"id": 2, "task": "Build an API"}]

@app.route("/todo",methods=["GET"])
def get_todo():
   
    return jsonify({
        "TODO" : todos
    })

@app.route("/todo/<int:todo_id>",methods=['GET'])
def get_specific_todo(todo_id):
    todo = None
    for item in todos:
        if item["id"] == todo_id:
            todo = item
            break

    if todo:
        return jsonify({
            "success": True,
            "message": f"Todo with ID {todo_id} found",
            "todo": todo
        }), 200
    else:
        return jsonify({
            "success" : False,
            "message": f"Todo with ID {todo_id} not found",
            "Error" : "Todo does exist"
        }),400
        
@app.route("/todos",methods=["POST"])
def create_todo():
    data = request.get_json()

    if len(todos) > 0:
        new_id = todos[-1]['id'] + 1
    else:
        new_id = 1


    new_todo = {
        "id" : new_id, "task" : data["task"]
    }

    todos.append(new_todo)

    return jsonify({
        "success": True,
        "message": f"Todo with id {new_id} added",
        "todo": new_todo
    }),201





if __name__ == "__main__":
    app.run(debug=True)