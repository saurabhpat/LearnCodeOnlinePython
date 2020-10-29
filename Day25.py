# Question :
# Write a python method to check whether a string is a valid password or not.
# Password Rules:
# Should have at least one number.
# Should have at least one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 6 to 20 Characters long.

# References :
# https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
# https://www.geeksforgeeks.org/password-validation-in-python/

def password_validity(passwd):
    if 6 < len(passwd) < 20:
        flag = True
    else:
        flag = False
    if not any(p.isdigit() for p in passwd):
        flag = False
    if not any(p.isupper() for p in passwd):
        flag = False
    if not any(p.islower() for p in passwd):
        flag = False
    if not any(p in '[@_!#$%^&*()<>?/|\\}{~:]' for p in passwd):
        flag = False

    if flag:
        return True
    else:
        return False


password = "Abc@123"
if password_validity(password):
    print("Password is valid")
else:
    print("Password is invalid")
