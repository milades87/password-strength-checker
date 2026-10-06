def check_password_strength(password):
    common_passwords = ['password', 'abc123', 'password1']

    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    if password in common_passwords:
        return "Weak: Password is very common."

    return "Strong: Password meets all criteria."


password = input("Enter a password to check: ")
result = check_password_strength(password)
print(result)