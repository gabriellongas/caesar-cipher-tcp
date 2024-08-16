def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def caesar_encrypt(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isalpha(): # check if is letter
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset - shift) % 26 + offset)
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)