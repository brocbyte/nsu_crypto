import sys
import math

import random
import string

import os

# generators
def generate_random_ascii_file(file_path, num_chars):
    with open(file_path, 'w') as file:
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=num_chars))
        file.write(random_chars)

def generate_random_bits_file(file_path, num_bits):
    with open(file_path, 'wb') as file:
        random_bits = bytearray(random.getrandbits(8) for _ in range(num_bits))
        file.write(random_bits)

def calculate_entropy(data):
    byte_freq = {}
    for byte in data:
        if byte in byte_freq:
            byte_freq[byte] += 1
        else:
            byte_freq[byte] = 1

    # Calculate probability of each byte
    total_bytes = len(data)
    byte_prob = {byte: freq / total_bytes for byte, freq in byte_freq.items()}
    alphabet_size = len(byte_prob)
    print(f"alphabet size: {alphabet_size}")
    print(f"log2(alphabet size): {math.log2(alphabet_size)}")

    # Calculate entropy
    entropy = -sum(prob * math.log2(prob) for prob in byte_prob.values())

    return entropy


if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit(-1)
    working_dir = sys.argv[1]
    generate_random_ascii_file(os.path.join(working_dir, "random_ascii.txt"), 10000)
    generate_random_bits_file(os.path.join(working_dir, "random_bits.txt"), 10000)
    filenames = next(os.walk(".\\entropy_examples"), (None, None, []))[2]
    print(f"Analyzing files {filenames}")
    for fname in filenames:
        print(f"=============== report for {fname} ===============")
        with open(os.path.join(working_dir, fname), mode = 'rb') as f:
            data = f.read()
            entropy = calculate_entropy(data)
            print(f"entropy: {entropy}")

