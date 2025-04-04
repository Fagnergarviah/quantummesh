class ZkSNARK:
    def __init__(self):
        self.setup_done = False

    def setup(self):
        # Implementação simplificada
        self.setup_done = True

    def generate_proof(self, secret: int) -> tuple:
        return (hash(secret), hash(secret * 2)) if self.setup_done else None
