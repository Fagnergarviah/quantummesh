from blockchain.chain import Blockchain
from blockchain.block import Block

def test_chain_initialization():
    chain = Blockchain()
    assert len(chain.chain) == 1  # Genesis block
    
def test_add_block():
    chain = Blockchain()
    chain.add_block([{"data": "test"}])
    assert len(chain.chain) == 2

