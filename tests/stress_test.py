import unittest
import time
from blockchain.block import Block

class TestBlockchain(unittest.TestCase):
    def test_block_creation(self):
        block = Block(1, time.time(), [], "genesis_hash")
        self.assertTrue(len(block.hash()) == 64)  # SHA-256 deve ter 64 chars hex
        self.assertIsInstance(block.hash(), str)
