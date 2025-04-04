class NodeDiscovery:
    def __init__(self):
        self.peers = []

    def discover(self, seed_nodes: list):
        for seed in seed_nodes:
            self.peers.extend(self._ping_seed(seed))  # Simulação

    def _ping_seed(self, seed: str) -> list:
        return [f"node_{i}" for i in range(2)]  # Mock
