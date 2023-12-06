import socket
import threading
from assets import platform
from player import player

class Server(threading.Thread):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        print(f"##############Server listening on {self.host}:{self.port}")
        self.bloc_checked = False
        
        self.data = {
            "players": [],
            "platforms": [],
            "blocs": [],
        }
        self.data["blocs"].append(platform.Cube(200, 200, 50))

    def start(self): # on écoute les connexions entrantes
        self.server_socket.listen(5)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"{client_socket} {client_address}")
            print(f"Accepted connection from {client_address}")
            # client_handler = ClientHandler(client_socket)
            # client_handler.start()

    def send_data(self, data):
        self.data = data
        socket.send(data)

    @property
    def players(self):
        return self.data["players"]

    @property
    def platforms(self):
        return self.data["platforms"]
    
    @property
    def blocs(self):
        result = self.data["blocs"]
        self.data["blocs"] = []
        return result
