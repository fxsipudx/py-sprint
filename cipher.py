def caesar_cipher(text,shift):
    answer = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text.lower():
        if char == " ":
            answer += " "
        elif char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            answer += alphabet[new_index]
    return answer    
print(caesar_cipher("hello world", 3))        
    