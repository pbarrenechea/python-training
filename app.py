from todos import todos
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        todos.create_todo(request.form['data'])
        return jsonify('Ok')
    elif request.method == 'GET':
        return jsonify(todos.list_todos())
if __name__ == '__main__':
    app.run()
    db.close()