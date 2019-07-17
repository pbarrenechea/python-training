from modules import todos
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def insert_todo():
    return jsonify(todos.list_todos())

@app.route('/hello', methods = ['POST'])
def list_todos():
   todos.create_todo(request.form['data'])
   return jsonify('Ok') 

if __name__ == '__main__':
    app.run()