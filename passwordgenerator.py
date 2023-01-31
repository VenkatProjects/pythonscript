import random
import string

def generate_password(length=8):
    """Generate a random password with a given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Example usage
password = generate_password(12)
print(password)

