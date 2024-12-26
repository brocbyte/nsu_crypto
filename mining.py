import hashlib
import time

def hash(value):
    hashGen = hashlib.sha256()
    hashGen.update(value.to_bytes(256 // 8, 'little'))
    return int(hashGen.hexdigest(), 16)

def mine(value, k, n):
    startTime = time.time()
    mask = ((1 << n) - 1) & (~((1 << (n - k)) - 1))
    nonce = 0
    while (hash(value | nonce) & mask) != 0:
        nonce += 1
    return nonce, time.time() - startTime

def main():
    t = int(input())
    k = 1
    value = 0x145
    n = 256
    for i in range(1, n):
        _, timeTaken = mine(value, i, n)
        print(f"checking k = {i}: {timeTaken} seconds...")
        if timeTaken >= t:
            k = i
            break
    while True:
        nonce, timeTaken = mine(value, k, n)
        print(f"block {nonce} for {timeTaken} seconds")

if __name__ == "__main__":
    main()
