from typing import List, Dict
from lib.db.config import createConnection

def authExists(username = None):
    return requestAuthDB(f'SELECT * FROM auth WHERE username="{username}"')
    
def createAuth(username = None, password = None):
    insertDB(f"INSERT INTO auth(username, passwd) VALUES ('{username}', '{password}')")
    return authExists(username)

def getUsers(start = None, name = None, username = None) -> List[Dict]:
    query = 'SELECT * FROM users'
    if name is not None:
        query += ' WHERE fullname LIKE "%' + name + '%"'
    if name is None and username is not None:
        query += ' WHERE username LIKE "%' + username + '%"'
    query += ' LIMIT ' + str(start) + ', 15'
    return requestDB(query)
    
def requestDB(query) -> List[Dict]:
    users = None
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    users = [{
        'id': userid,
        'name': fullname,
        'username': username
    } for (userid, fullname, username) in cursor]
    cursor.close()
    connection.close()
    return users
    
def requestAuthDB(query) -> Dict:
    users = None
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    users = [{
        'id': id,
        'username': username,
        'password': passwd
    } for (id, username, passwd) in cursor]
    cursor.close()
    connection.close()
    if users:
        return users[0]
    return None
        
    
def insertDB(query) -> None:
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    
def countDB(name = None, username = None) -> str:
    query = 'SELECT COUNT(*) FROM users'
    if name is not None:
        query += ' WHERE fullname LIKE "%' + name + '%"'
    if name is None and username is not None:
        query += ' WHERE username LIKE "%' + username + '%"'
        
    total = None
    connection = createConnection()
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    total = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return str(total)
    