import string
import random

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_passwords(passwords, filename):
    with open(filename, 'w') as f:
        for i, password in enumerate(passwords, start=1):
            f.write(f"Password {i}: {password}\n")
    print(f"Passwords saved to {filename}")

def main():
    print("Welcome to Advanced Password Generator")
    
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    count = int(input("Number of passwords to generate: "))

    passwords = []
    for x in range(count):
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
        passwords.append(password)

    save_choice = input("Save passwords to file? (y/n): ").lower() == 'y'
    if save_choice:
        filename = input("Enter filename (default: passwords.txt): ") or "passwords.txt"
        save_passwords(passwords, filename)

if __name__ == '__main__':
    main()