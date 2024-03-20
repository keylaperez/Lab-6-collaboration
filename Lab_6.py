# name: Keyla Perez
# Encoder function
def encode(password):
    """
    Encode the password by shifting each digit up by 3 numbers.
    """
    encoded_password = ""
    for digit in password:
        encoded_digit = int(digit)
        if encoded_digit == 9:
            encoded_digit = 2  # Wrap around from 9 to 2
        elif encoded_digit == 8:
            encoded_digit = 1  # Wrap around from 8 to 1
        elif encoded_digit == 7:
            encoded_digit = 0  # Wrap around from 7 to 0
        else:
            encoded_digit += 3  # Shift digit up by 3
        encoded_password += str(encoded_digit)
    return encoded_password

# Name: Shamsuddin Shaikh
def decode_password(encoded_password):
    password = ""
    for digit in encoded_password:
        decoded_password = str((int(digit) - 3) % 10)  # shift each digit down by 3 numbers
        password += decoded_password
    return password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password! Please enter 8-digit password containing only integers.")
                continue
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            # Main choice 2, Shamsuddin Shaikh
        elif choice == "2":
            if not encoded_password:
                print("Please encode a password first (Option 1).")
            else:
                print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

