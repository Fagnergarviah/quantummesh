import unittest
import time
from mesh_network.propagation import MessagePropagator

class TestNetwork(unittest.TestCase):
    def test_propagation(self):
        propagator = MessagePropagator()
        nodes = ["node1", "node2", "node3"]
        
        # Teste inicial
        self.assertEqual(propagator.propagate("test1", nodes), 3)
        
        # Teste de mensagem duplicada
        self.assertEqual(propagator.propagate("test1", nodes), 0)
