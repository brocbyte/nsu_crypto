import os
from arc4 import ARC4
import filecmp
RAND_MAX = 256

def rand():
    rand.next = rand.next * 1103515245 + 12345
    return (rand.next // 65536) % (RAND_MAX + 1);
rand.next = 1

def generate_random_file(filename, size):
    with open(filename, 'wb') as file:
        for _ in range(size):
            symbol = rand()
            file.write(bytearray([symbol]))

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
def generate_lorem_ipsum_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def vernam_cipher_encrypt(input_file, key_file, output_file):
    with open(input_file, 'rb') as input_f, open(key_file, 'rb') as key_f, open(output_file, 'wb') as output_f:
        for char, key_char in zip(input_f.read(), key_f.read()):
            ciphered_char = bytearray([char ^ key_char])
            output_f.write(ciphered_char)

def vernam_cipher_decrypt(input_file, key_file, output_file):
    with open(input_file, 'rb') as input_f, open(key_file, 'rb') as key_f, open(output_file, 'wb') as output_f:
        for char, key_char in zip(input_f.read(), key_f.read()):
            decrypted_char = bytearray([char ^ key_char])
            output_f.write(decrypted_char)


if __name__ == "__main__":
    folder = ".\\vernam_cipher_examples"
    txt_fname = os.path.join(folder, "lorem.txt")
    key_fname = os.path.join(folder, "key.bin")
    enc_fname = os.path.join(folder, "lorem.enc")
    dec_fname = os.path.join(folder, "lorem.dec")
    generate_lorem_ipsum_file(txt_fname, txt)
    generate_random_file(key_fname, len(txt))
    vernam_cipher_encrypt(txt_fname, key_fname, enc_fname)
    vernam_cipher_decrypt(enc_fname, key_fname, dec_fname)
    print(f"Are files equal? {filecmp.cmp(txt_fname, dec_fname)}")

    plain_text = b'some plain text to encrypt'
    print(f"plain_text: {plain_text}")
    print(f"len(plain_text): {len(plain_text)}")
    arc4 = ARC4(b'secret_key')
    enc = arc4.encrypt(plain_text)
    print(f"len(enc): {len(enc)}")
    arc4 = ARC4(b'secret_key')
    dec = arc4.decrypt(enc)
    print(f"dec: {dec}")