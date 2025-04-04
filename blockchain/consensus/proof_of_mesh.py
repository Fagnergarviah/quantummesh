import hashlib
from typing import List, Dict

class ProofOfMesh:
    def __init__(self):
        self.node_reputation: Dict[str, float] = {}  # {node_id: reputation_score}
    
    def update_reputation(self, node_id: str, success: bool):
        """Atualiza reputação baseada em contribuições à rede mesh."""
        if node_id not in self.node_reputation:
            self.node_reputation[node_id] = 0.5  # Valor inicial
        self.node_reputation[node_id] += 0.1 if success else -0.2
    
    def select_validator(self) -> str:
        """Seleciona validador baseado em reputação + stake (PoS)."""
        from random import choices
        nodes, weights = zip(*self.node_reputation.items())
        return choices(nodes, weights=weights, k=1)[0]
