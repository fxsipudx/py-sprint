alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "hello world"
shift = 3
answer = ""

for char in text.lower():
    if char in alphabet:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        answer += alphabet[new_index]
print(answer)        
    