#Klient Opgave 5

from socket import *
import json

servername = "localhost"
serverport = 10

clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername, serverport))

request = {
    'operation': input("Enter operation (Add, Random, or Subtract):"),
    'num1': int(input('Enter number 1:')),
    'num2': int(input('Enter number 2:'))
}

data = json.dumps(request).encode()
clientsocket.send(data)

datatilbage = clientsocket.recv(2048)
response = json.loads(datatilbage.decode())

if 'Result' in response:
    print("Received result:", response['Result'])
else:
    print("Received error:", response['Error'])

clientsocket.close()
