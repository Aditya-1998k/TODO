from flask import Flask, request, jsonify
from todos import get_todos, add_todo, delete_todo, modify_todo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/todos',methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'GET':
        return jsonify(get_todos())
    
    elif request.method == 'POST':
        data =request.json
        add_todo(data)
        return jsonify({"message":"data added successfully"})
    
@app.route('/api/todos/<int:index>', methods=['DELETE', 'PUT'])
def handle_todos_index(index):
    if request.method == 'DELETE':
        delete_todo(index)
        return jsonify({"message":"todo deleted successfully"})
    
    elif request.method =='PUT':
        data =request.json
        modify_todo(index, data['text'])
        return jsonify({"message": "modified successfully"})



if __name__=='__main__':
    app.run(port=4547, debug=True)