
"""
This is a User Rgistration System for a website.
"""
# Solution 1
users = []
def register_user(username, password, email):
    """This functiion is used to register new users and it takes three parameters
    username, password, email. New users are created using the information supplied and stored in a global list called users.
    Each user is represented as a dictionary with keys; 'username', 'password' and 'email'.
    """
    dict = {}
    dict["username"] = username
    dict["password"] = password
    dict["email"] = email
    
    users.append(dict)
    
register_user("john123", "pass123", "john@example.com")
register_user("emma456", "abc456", "emma@example.com")
register_user("james789", "xyz789", "james@example.com")

print(users)

# Solution 2
def login_user(username, password):
    """This function searches for a user with the given username in the users list and checks
    if the corresponding password matches. If a matching user is found, it prints "Login successful!". 
    Otherwise, prints "Invalid username or password."""
    for user in users:
        if (username == user['username']):
            if (password == user['password']):
                print('Login successful')
            else:
                print('invalid login or password')

login_user("john123", "pass123")
login_user("emma456", "wrongpass")
login_user("james789", "xyz789")

# Solution 3
def change_password(username, old_password, new_password):
    """This function finds the user with the given username in the users list and check if the old_password matches.
    If it does, it updates the user's password with the new_password and print "Password changed successfully!
    But If the old_password doesn't match, it prints "Invalid password.
    """
    for user in users:
        if (username == user['username']):
            if (old_password == user['password']):
                old_password = new_password
                print('Password changed successfully!')
            else:
                print('Invalid password')

change_password("john123", "pass123", "newpass")
change_password("emma456", "wrongpass", "newpass")
