from oqs import sig

DILITHIUM_ALG = "Dilithium2"

def generate_keys():
    public_key, secret_key = sig.generate_keypair(DILITHIUM_ALG)
    return public_key, secret_key

def sign_transaction(secret_key, message):
    signature = sig.sign(message, secret_key, DILITHIUM_ALG)
    return signature

def verify_transaction(public_key, message, signature):
    try:
        sig.verify(message, signature, public_key, DILITHIUM_ALG)
        return True
    except:
        return False
