import os
from tronpy import Tron
from tronpy.keys import PrivateKey

PRIV_KEY = os.getenv("TRON_KEY", "d7495b9abd05be025749bb5e6d3c83aa45f4f0d948a0e2d96d9f99f8131a70e2")
SENDER = "TUL16qQxphAR8nEYVy6wdRadZobZmbP5fs"
USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"

client = Tron()

def send_usdt(to, amount_usdt):
    priv = PrivateKey(bytes.fromhex(PRIV_KEY))
    usdt = client.get_contract(USDT_CONTRACT)
    txn = usdt.functions.transfer(to, int(amount_usdt * 1e6))
    txn = txn.with_owner(SENDER).fee_limit(30_000_000).build().sign(priv)
    return txn.broadcast()

if __name__ == "__main__":
    import sys
    to = sys.argv[1]
    amt = float(sys.argv[2])
    print(f"Sending {amt} USDT to {to}...")
    result = send_usdt(to, amt)
    print(f"TX: {result}")
