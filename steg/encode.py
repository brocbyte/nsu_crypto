#!/usr/bin/env python3
import random
import bitarray
from PIL import Image
import numpy as np

def generate_next_idx(arr_len):
    new_idx = random.randrange(0, arr_len)
    if new_idx in generate_next_idx.used_indices:
        prob_idx = new_idx + 1
        while True:
            if prob_idx in generate_next_idx.used_indices:
                prob_idx += 1
                prob_idx = prob_idx if prob_idx != arr_len else 0
            else:
                break
        generate_next_idx.used_indices.add(prob_idx)
        return prob_idx
    else:
        generate_next_idx.used_indices.add(new_idx)
        return new_idx

def encode(image_byte_array, message, secret_key):
    shape = image_byte_array.shape
    image_byte_array = image_byte_array.reshape(-1)
    print(f"Number of bytes: {image_byte_array.shape[0]}")

    #### Преобразуем сообщение: в начало всегда будем ставить длину сообщения, затем специальный символ
    message = str(len(message)) + "$" + message

    #### Получаем битовую строку из преобразованного сообщения
    bit_array = bitarray.bitarray()
    bit_array.frombytes(message.encode('ascii'))
    if len(bit_array) > image_byte_array.shape[0]:
        print("Your message is too long for such an image")
        exit(1)
    else:
        print(f"Your message is {len(bit_array)} bits ({len(bit_array) // 8} bytes) long")

    random.seed(secret_key)
    for bit in bit_array:
        byte_to_change = generate_next_idx(image_byte_array.shape[0])
        old_val = image_byte_array[byte_to_change]
        image_byte_array[byte_to_change] = old_val | 1 if bit else old_val & ~1
        # print("bit: " + str(bit) + " {0:b}".format(old_val) + " -> {0:b}".format(image_byte_array[byte_to_change]), end ="\n\n")
    image_byte_array = image_byte_array.reshape(shape)
    result = Image.fromarray(image_byte_array)
    result.save('./imgs/image_with_message.bmp')

if __name__ == '__main__':
    generate_next_idx.used_indices = set()
    #### Чтение изображения
    im = Image.open("./imgs/image.bmp")
    p = np.array(im)
    print(f"Shape: {p.shape}")
    print("Enter your message: ")
    message = input()
    # message = "m" * int(p.shape[0] * p.shape[1] * p.shape[2] // 8 * 0.3)
    print(len(message))
    print("Enter secret: ")
    secret = int(input())
    encode(p, message, secret)