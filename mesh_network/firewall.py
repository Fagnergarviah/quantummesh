from collections import defaultdict

class MeshFirewall:
    def __init__(self):
        self.suspicious_nodes = defaultdict(int)
    
    def detect_attack(self, node_ip: str, packet_count: int) -> bool:
        if packet_count > 1000:  # Limite de pacotes/segundo
            self.suspicious_nodes[node_ip] += 1
            return True
        return False
