#Server Opgave 5

from socket import *
import threading
import json
import random

def handleOneClient(connectionSocket, address):
    print('Address', address)

    data = connectionSocket.recv(2048).decode()
    
    try:
        request = json.loads(data)
        
        if 'operation' in request and 'num1' in request and 'num2' in request:
            operation = request['operation']
            num1 = int(request['num1'])
            num2 = int(request['num2'])

            if operation == 'Add':
                result = num1 + num2
            elif operation == 'Subtract':
                result = num1 - num2
            elif operation == 'Random':
                result = random.randint(num1, num2)
            else:
                result = 'Invalid input'

            response = {'result': result}
            connectionSocket.send(json.dumps(response).encode())
        else:
            connectionSocket.send(json.dumps({'error': 'Invalid input'}).encode())
    except json.JSONDecodeError:
        connectionSocket.send(json.dumps({'error': 'Invalid JSON'}).encode())

    connectionSocket.close()

serverPort = 10

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to work for you')

while True:
    clientSocket, clientAddress = serverSocket.accept()
    threading.Thread(target=handleOneClient, args=(clientSocket, clientAddress)).start()
