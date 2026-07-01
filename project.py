import random
import sys
#Project VaultText
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?"
original_siq = list(string)

def main():
    print()
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print()

    option = input("choose 1 or 2: ").strip()
    if option != "1" and option != "2":
        sys.exit(f"{option} is not an option")

    elif option == "1":
        massage = input("Type a message: ").strip()

        current_key = generate_key()
        current_key_string = "".join(current_key)

        with open("key.txt", "a") as file:
            file.write(f"{current_key_string}\n")
        print("key has been saved in key.txt")
        print()

        encrypt_msg = encrypt(massage, current_key)
        print(f"Encrypted Message: {encrypt_msg}")
        print()

    elif option == "2":
        d_key = input("Type the key: ")
        d_key = list(d_key)

        if len(d_key) != len(original_siq):
            sys.exit("Invalid key")

        e_msg = input("Type the message: ").strip()

        dicrypt_msg = dicrypt(e_msg, d_key)
        print(f"Decrypted Message: {dicrypt_msg}")
        print()

def generate_key():
    copy_key = original_siq.copy()
    random.shuffle(copy_key)
    return copy_key

def encrypt(msg, key):
    enc_msg = ""
    for letter in msg:
        if letter in original_siq:
            index = original_siq.index(letter)
            enc_msg = enc_msg + key[index]
        else:
            enc_msg = enc_msg + letter
    return enc_msg

def dicrypt(msg, key):
    dic_msg = ""
    for letter in msg:
        if letter in key:
            index = key.index(letter)
            dic_msg = dic_msg + original_siq[index]
        else:
            dic_msg = dic_msg + letter
    return dic_msg

if __name__ == "__main__":
    main()