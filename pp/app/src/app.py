from flask import Flask, request
from flask_cors import CORS, cross_origin
from lib.users import *
import json

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.route('/register', methods=['POST'])
def register() -> str:
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if authExists(username):
        return json.dumps({'success': False, 'message': 'Auth already exists'})
        
    createAuth(username, password)
    return json.dumps({'success': True, 'message': 'Auth successful'})
    
@app.route('/login', methods=['POST'])
def login() -> str:
    form = request.form
    username = form.get('username')
    password = form.get('password')
    auth = authExists(username)
    if not auth or (auth['password'] != password):
        return json.dumps({'success': False, 'message': 'Auth do not exists'})
    return json.dumps({'success': True, 'message': 'Login successful', 'data': auth})   

@app.route('/users', methods=['GET'])
def users() -> str:
    args = request.args
    start = args.get('start', 0)
    name = args.get('name', None)
    username = args.get('username', None)
    return json.dumps({'success': True, 'users': getUsers(int(start) * 15, name, username), 'total': countDB(name, username)})
    
@app.route('/users/total', methods=['GET'])
def totalUsers() -> str:
    return json.dumps({'success': True, 'users': countDB()})
    
@app.route('/', methods=['GET'])
def index() -> str:
    return 'Hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)