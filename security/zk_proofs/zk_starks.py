class ZKStark:
    """Implementação simulada de ZK-STARKs"""
    @staticmethod
    def generate_proof(secret: int) -> tuple:
        return (hash(str(secret)), hash(str(secret*2)))
    
    @staticmethod
    def verify(proof: tuple) -> bool:
        return proof[1] == hash(str(int(hash(proof[0]))*2))
