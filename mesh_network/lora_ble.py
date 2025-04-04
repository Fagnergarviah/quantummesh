import socket

class MeshNetwork:
    def __init__(self):
        self.nodes = set()
    
    def connect(self, node_ip: str):
        self.nodes.add(node_ip)
    
    def broadcast(self, message: str):
        for node in self.nodes:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((node, 5000))
                    s.sendall(message.encode())
            except:
                self.nodes.remove(node)
