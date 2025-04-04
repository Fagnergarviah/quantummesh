from typing import List
from blockchain.block import Block

class ConflictResolver:
    def resolve(self, chain_a: List[Block], chain_b: List[Block]) -> List[Block]:
        """Implementa a regra da cadeia mais longa"""
        return chain_a if len(chain_a) >= len(chain_b) else chain_b
