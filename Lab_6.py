# name: Keyla Perez
# Encoder function
def encode(password):
    """
    Encode the password by shifting each digit up by 3 numbers.

    Args:
    password (str): The 8-digit password in string format containing only integers.

    Returns:
    str: The encoded password.
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
        elif choice == "2":
            # Placeholder for decoder function
            print("Decoder function is not implemented yet.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

