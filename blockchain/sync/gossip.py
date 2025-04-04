import random

class GossipProtocol:
    def __init__(self):
        self.known_messages = set()

    def broadcast(self, message: str, nodes: list):
        for node in random.sample(nodes, min(3, len(nodes))):  # Propaga para 3 nós aleatórios
            node.send(message)
            self.known_messages.add(hash(message))
