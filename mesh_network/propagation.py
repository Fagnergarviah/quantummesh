import random
from typing import List

class MessagePropagator:
    def __init__(self):
        self.seen_messages = set()

    def propagate(self, message: str, nodes: List[str]) -> int:
        """Propaga mensagem para nós aleatórios, retorna número de nós alcançados"""
        if message in self.seen_messages:
            return 0
            
        self.seen_messages.add(message)
        targets = random.sample(nodes, min(3, len(nodes)))
        return len(targets)  # Simulação: todos os nós recebem
