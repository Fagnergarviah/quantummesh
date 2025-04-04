from security.pqc.dilithium import generate_keys
from typing import Tuple

class Wallet:
    def __init__(self):
        self.public_key, self.private_key = generate_keys()
    
    def get_address(self) -> str:
        return self.public_key.hex()[:40]  # Endereço reduzido
