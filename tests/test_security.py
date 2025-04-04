import pytest
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

# --- Implementação das Funções ---
def generate_keys():
    """Gera um par de chaves Ed25519 (pública e privada)."""
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    
    # Serializa as chaves para bytes (opcional: pode retornar os objetos diretamente)
    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    return pub_bytes, priv_bytes

def sign_transaction(private_key_bytes, message):
    """Assina uma mensagem com a chave privada."""
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)
    return private_key.sign(message)

def verify_signature(public_key_bytes, message, signature):
    """Verifica uma assinatura com a chave pública."""
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_key_bytes)
    try:
        public_key.verify(signature, message)
        return True
    except InvalidSignature:
        return False

# --- Testes ---
def test_crypto_operations():
    """Testa operações básicas de criptografia."""
    pub, priv = generate_keys()
    assert isinstance(pub, bytes) and isinstance(priv, bytes)
    assert len(pub) == 32 and len(priv) == 32  # Tamanho das chaves Ed25519

def test_signature_verification():
    """Testa a assinatura e verificação de uma mensagem."""
    pub, priv = generate_keys()
    message = b"test_message"
    signature = sign_transaction(priv, message)
    
    # Verificação positiva
    assert verify_signature(pub, message, signature)
    
    # Verificação negativa (mensagem alterada)
    assert not verify_signature(pub, b"wrong_message", signature)
    
    # Verificação negativa (assinatura alterada)
    corrupted_signature = bytes([b ^ 1 for b in signature])  # Altera 1 byte
    assert not verify_signature(pub, message, corrupted_signature)

if __name__ == "__main__":
    pytest.main(["-v"])
