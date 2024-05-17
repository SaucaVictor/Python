import random
import hashlib
import ecdsa
import base58
already_checked=[]
adress="13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
start = pow(2,65)
end = pow(2,66)-1

for i in range(start,end):
    random_number = random.randint(start,end)
    hex_string = hex(random_number)[2:].upper()
    padded_hex_string = hex_string.zfill(64)
    print(random_number ,padded_hex_string)
    def hash256(hex_string):
        binary = bytes.fromhex(hex_string)
        hash1 = hashlib.sha256(binary).digest()
        hash2 = hashlib.sha256(hash1).digest()
        result = hash2.hex()
        return result
    def checksum(hex_string):
        hash_result = hash256(hex_string) 
        return hash_result[:8]  
    def base58_encode(hex_string):
        chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        base = len(chars)
        i = int(hex_string, 16)
        buffer = ""
        while i > 0:
            remainder = i % base
            i = i // base
            buffer = chars[remainder] + buffer
        leading_zero_bytes = len(hex_string) - len(hex_string.lstrip('0'))
        buffer = "1" * (leading_zero_bytes // 2) + buffer
        return buffer
    private_key = str(padded_hex_string) 
    data = "80" + private_key
    data += "01"
    data += checksum(data)
    wif = base58_encode(data)
    print(wif) 
    def is_valid_private_key(private_key_hex):
        try:
            int(private_key_hex, 16)
        except ValueError:
            return False
        n = ecdsa.curves.SECP256k1.order
        private_key_int = int(private_key_hex, 16)
        if private_key_int >= 1 and private_key_int < n:
            return True
        else:
            return False
    def generate_public_key(private_key_hex, compressed=True):
        curve = ecdsa.curves.SECP256k1
        private_key_bytes = bytes.fromhex(private_key_hex)
        signing_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=curve)
        verifying_key = signing_key.verifying_key
        if compressed:
            public_key = verifying_key.to_string("compressed").hex()
        else:
            public_key = verifying_key.to_string("uncompressed").hex()
        return public_key
    
    private_key_hex = str(padded_hex_string)
    public_key = generate_public_key(private_key_hex, compressed=True)
    
    if is_valid_private_key(private_key_hex):
        print("Corresponding public key (compressed):", public_key)
    else:
        print("Private key is not valid.")
    def generate_address(public_key_compressed):
        sha256_hash = hashlib.sha256(bytes.fromhex(public_key_compressed)).digest()
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
        network_byte = b'\x00'
        hashed_public_key = network_byte + ripemd160_hash
        double_sha256_hash = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()
        checksum = double_sha256_hash[:4]
        binary_address = hashed_public_key + checksum
        bitcoin_address = base58.b58encode(binary_address)
        return bitcoin_address.decode()
    public_key_compressed = str(public_key)
    bitcoin_address = generate_address(public_key_compressed)
    print("Bitcoin address:", bitcoin_address)
    print('\n\n')
    if adress == str(bitcoin_address):
        print("Adress found")
        break
