def encode_name(name):
    encoded = ""
    for char in name:
        if char.isalpha():
            encoded += str(ord(char.lower()) - 96) + " "
        else:
            encoded += char + " "
    return encoded.strip()

def decode_name(encoded):
    decoded = ""
    nums = encoded.split()
    for num in nums:
        if num.isdigit():
            decoded += chr(int(num) + 96)
        else:
            decoded += num
    return decoded

name = input("Enter your name: ")
encoded_name = encode_name(name)
print("Encoded name:", encoded_name)

decoded_name = decode_name(encoded_name)
print("Decoded name:", decoded_name)
