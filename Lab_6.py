# This program implements a simple password encoder/decoder

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
        encoded_digit = str((int(digit) + 3) % 10)  # Shift digit up by 3 and wrap around if needed
        encoded_password += encoded_digit
    return encoded_password
