def caesar(s, key):
    return "".join([chr(((ord(c) - ord('a') + key) % 26) + ord('a')) if c.isalpha() else c for c in s])
print(caesar("test", 0) == "test")
print(caesar("test", 1) == "uftu")
print(caesar("test", 17) == "kvjk")
print(caesar("test", -17) == "cnbc")
print(caesar("test", 25) == "sdrs")
print(caesar(caesar("test", 15), -15) == "test")
print(caesar(caesar("test", 25), -25) == "test")

def known_plaintext_attack(cipherText, plainText):
    for key in range(26):
        if (caesar(plainText, key) == cipherText):
            return key
    raise "..." 

print(known_plaintext_attack("test", "test") == 0)
print(known_plaintext_attack("uftu", "test") == 1)
print(known_plaintext_attack("kvjk", "test") == 17)

def ciphertext_only_attack(cipherText, dictionary = []):
    print("======================")
    print(f"dictionary: {dictionary}")
    for key in range(26):
        plaintext = caesar(cipherText, -key)
        if len(dictionary) == 0 or [item for item in dictionary if item in plaintext]:
            print(f"key {key}: {plaintext}")
    print("======================")


ciphertext_only_attack("uftu")
ciphertext_only_attack("uftu", ["test"])

long_plaintext = "if he had anything confidential to say," \
    " he wrote it in cipher, that is, by so changing" \
    " the order of the letters of the alphabet, that not a word could be made out."
long_ciphertext = caesar(long_plaintext, 15)

ciphertext_only_attack(long_ciphertext)
ciphertext_only_attack(long_ciphertext, ["it"])