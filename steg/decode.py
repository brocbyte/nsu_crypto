#!/usr/bin/env python3
import random
import bitarray
from PIL import Image
import numpy as np

from encode import generate_next_idx

def decode(image_byte_array, secret_key):
    random.seed(secret_key)
    collected_bits = []
    left_to_read = -1 
    while(True):
        for _ in range(8):
            idx = generate_next_idx(image_byte_array.shape[0])
            collected_bits.append(image_byte_array[idx] & 1)
        if left_to_read > 0:
            left_to_read -= 1
        decoded_string = bitarray.bitarray(collected_bits).tobytes().decode('ascii')
        if decoded_string[-1] == '$':
            left_to_read = int(decoded_string[:-1])
            print(f"Original message length: " + str(left_to_read))
        if left_to_read == 0:
            break
    decoded_string = bitarray.bitarray(collected_bits).tobytes().decode('ascii')
    decoded_string = decoded_string[decoded_string.index("$")+1:]
    print(f"Decoded message: " + decoded_string)

if __name__ == "__main__":
    generate_next_idx.used_indices = set()
    #### Чтение изображения
    im = Image.open("./imgs/image_with_message.bmp")
    p = np.array(im)
    print(f"Shape: {p.shape}")
    height, width, depth = p.shape
    p = p.reshape(-1)

    #### Считаем количество изменяемых байт (размер контейнера в битах)
    number_of_pixels = p.shape[0]
    print(f"Number of bytes: {number_of_pixels}")
        
    print("Enter secret: ")
    secret = int(input())
    decode(p, secret)