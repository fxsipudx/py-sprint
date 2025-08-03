def caesar_cipher(text,key,direction = 1):
    key_index = 0
    answer = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text.lower():
        if not char.isalpha():
            answer += char
        elif char in alphabet:
            key_char = key[key_index % len(key)]
            key_index += 1
            shift = alphabet.find(key_char)
            index = alphabet.find(char)
            new_index = (index + direction * shift) % len(alphabet)
            answer += alphabet[new_index]
    return answer    
def encrypt(message,key):
    return caesar_cipher(message,key)  
def decrypt(message,key):
    return caesar_cipher(message,key,-1)
     
msg = "Hello, World!"
key = "abc"

encrypted = encrypt(msg, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)