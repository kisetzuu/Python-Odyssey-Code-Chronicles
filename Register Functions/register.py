# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)
print("--------------------\n")

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)
print("--------------------\n")

# Start coding here
def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError('The username is not validated.')
    
    if not validate_email(email):
        raise ValueError('The email is not validated.')
        
    if not validate_password(password):
        raise ValueError('The password is not validated')
    
    return True

def register_user(name, email, password):
    try:
        if validate_user(name, email, password):
            user = {
                "name": name,
                "email": email,
                "password": password
            }
            return user
    except ValueError as e:
        print(f"User Registration Failed! {e}")
        return False
