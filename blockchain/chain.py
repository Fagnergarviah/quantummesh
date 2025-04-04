import time
from typing import List, Dict
from blockchain.block import Block
from .block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self) -> Block:
        return Block(0, time.time(), [], "0")
    
    def add_block(self, transactions: List[Dict]) -> Block:
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            transactions=transactions,
            previous_hash=last_block.hash()
        )
        self.chain.append(new_block)
        return new_block
