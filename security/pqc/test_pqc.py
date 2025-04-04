import sys
sys.path.insert(0, "security/pqc")

from dilithium import *
from kyber import *
import pytest

def test_kyber_keygen():
    pk, sk = kyber_keygen()
    assert len(pk) > 0 and len(sk) > 0

def test_dilithium_sign():
    pk, sk = dilithium_keygen()
    msg = b"test"
    sig = dilithium_sign(sk, msg)
    assert dilithium_verify(pk, msg, sig)
