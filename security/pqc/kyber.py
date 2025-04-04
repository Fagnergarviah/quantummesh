from oqs import kem

KYBER_ALG = "Kyber512"

def kyber_keygen():
    public_key, secret_key = kem.generate_keypair(KYBER_ALG)
    return public_key, secret_key

def kyber_encrypt(public_key):
    ciphertext, shared_secret = kem.encap_secret(public_key, KYBER_ALG)
    return ciphertext, shared_secret

def kyber_decrypt(secret_key, ciphertext):
    shared_secret = kem.decap_secret(ciphertext, secret_key, KYBER_ALG)
    return shared_secret
