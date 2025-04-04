from dataclasses import dataclass
import hashlib
from security.pqc.dilithium import generate_keys, sign_transaction, verify_transaction  # Corrigido

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    signature: bytes = None
    tx_id: str = None

    def __post_init__(self):
        self.tx_id = self._generate_id()

    def _generate_id(self) -> str:
        return hashlib.sha256(f"{self.sender}{self.receiver}{self.amount}".encode()).hexdigest()

    def sign(self, private_key: bytes):
        self.signature = sign_transaction(private_key, self.tx_id.encode())

    def is_valid(self) -> bool:
        return verify_transaction(self.sender.encode(), self.tx_id.encode(), self.signature)
