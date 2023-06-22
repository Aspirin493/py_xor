import random

MAX_XOR_STR_COUNT = 256

def xor_cipher(message, key):
    ciphertext = ""
    for i in range(len(message)):
        # Применяем операцию XOR к каждому символу сообщения и ключу
        # и добавляем результат в зашифрованную строку
        ciphertext += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def generate_xor_string():
    key = random.randint(1, 255)
    length = random.randint(1, MAX_XOR_STR_COUNT)
    plaintext = ''.join([chr(random.randint(0, 255)) for _ in range(length)])
    ciphertext = ''.join([chr(ord(c) ^ key) for c in plaintext])
    return key, ciphertext

if __name__ == '__main__':
    for i in range(10):
        key, ciphertext = generate_xor_string()
        print(f'Key: {key}, Ciphertext: {ciphertext}')
