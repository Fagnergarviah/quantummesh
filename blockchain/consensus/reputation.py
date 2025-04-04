import time
from typing import Dict

class ReputationSystem:
    def __init__(self):
        self.node_scores: Dict[str, float] = {}
        self.last_activity: Dict[str, float] = {}
        
    def update_reputation(self, node_id: str, behavior_score: float):
        """Atualiza a reputação de um nó baseado em seu comportamento"""
        current_time = time.time()
        
        # Decaimento da reputação ao longo do tempo
        if node_id in self.node_scores:
            time_elapsed = current_time - self.last_activity.get(node_id, current_time)
            decay_factor = max(0.9, 1 - (time_elapsed / 86400))  # Decai 10% por dia
            self.node_scores[node_id] *= decay_factor
        
        # Atualiza com novo score
        self.node_scores[node_id] = self.node_scores.get(node_id, 1.0) * behavior_score
        self.last_activity[node_id] = current_time
        
        # Garante que a reputação fique entre 0 e 1
        self.node_scores[node_id] = max(0.0, min(1.0, self.node_scores[node_id]))
    
    def get_reputation(self, node_id: str) -> float:
        """Retorna a reputação atual do nó"""
        return self.node_scores.get(node_id, 0.5)  # Valor padrão para novos nós
    
    def penalize_node(self, node_id: str, penalty: float = 0.1):
        """Aplica penalidade a um nó por comportamento malicioso"""
        self.update_reputation(node_id, 1 - penalty)
