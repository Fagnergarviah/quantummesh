import json
from typing import Dict, List
import hashlib

class DTNProtocol:
    def __init__(self):
        self.message_store: Dict[str, dict] = {}
        
    def store_message(self, message: dict) -> str:
        """Armazena mensagem para entrega posterior"""
        message_hash = hashlib.sha256(json.dumps(message).encode()).hexdigest()
        self.message_store[message_hash] = {
            'message': message,
            'timestamp': time.time(),
            'delivered': False
        }
        return message_hash
    
    def get_pending_messages(self, max_age: int = 86400) -> List[dict]:
        """Retorna mensagens não entregues dentro do período especificado"""
        current_time = time.time()
        return [
            msg['message'] for msg in self.message_store.values()
            if not msg['delivered'] and (current_time - msg['timestamp']) <= max_age
        ]
    
    def mark_as_delivered(self, message_hash: str):
        """Marca mensagem como entregue"""
        if message_hash in self.message_store:
            self.message_store[message_hash]['delivered'] = True
