import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'pp'
}

def createConnection():
    connection = mysql.connector.connect(**config)
    return connection