class StakeManager:
    def __init__(self):
        self.stakes = {}  # {node_id: amount_staked}
    
    def add_stake(self, node_id: str, amount: float):
        self.stakes[node_id] = self.stakes.get(node_id, 0) + amount
