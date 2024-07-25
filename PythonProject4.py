//Decoded name. Multiples

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

def erase_name():
    global name
    name = ""

while True:
    print("1. Enter name")
    print("2. Encode name")
    print("3. Decode name")
    print("4. Erase name")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
    elif choice == "2":
        if not name:
            print("Please enter a name first.")
        else:
            encoded_name = encode_name(name)
            print("Encoded name:", encoded_name)
    elif choice == "3":
        if not name:
            print("Please enter a name first.")
        else:
            decoded_name = decode_name(name)
            print("Decoded name:", decoded_name)
    elif choice == "4":
        erase_name()
        print("Name erased.")
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")