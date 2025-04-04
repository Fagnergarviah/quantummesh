class SPVClient:
    def __init__(self):
        self.block_headers = []

    def verify_tx(self, tx_id: str, merkle_proof: list) -> bool:
        return tx_id in merkle_proof  # Simulação simplificada
