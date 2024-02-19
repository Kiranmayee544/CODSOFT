import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
            elif length > 15:
                print("Length is exceeded. decrease the length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print("Generated password:", password)
