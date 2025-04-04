class UTXOSet:
    def __init__(self):
        self.utxos = {}  # {tx_id: {output_index: (amount, address)}}

    def add_utxo(self, tx_id: str, output_index: int, amount: float, address: str):
        if tx_id not in self.utxos:
            self.utxos[tx_id] = {}
        self.utxos[tx_id][output_index] = (amount, address)

    def spend_utxo(self, tx_id: str, output_index: int):
        if tx_id in self.utxos and output_index in self.utxos[tx_id]:
            del self.utxos[tx_id][output_index]
