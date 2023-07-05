# 04-07-2023-Python-Function-parameters-III


Task : User Registration System
You are tasked with creating a user registration system for a website. Implement the following functions:

1. `register_user(username, password, email)`: This function takes in three parameters: `username`, `password`, and `email`. It should create a new user with the given information and store it in a global list called `users`. Each user should be represented as a dictionary with keys "username", "password", and "email". Test the function by registering a few users and printing the `users` list.

2. `login_user(username, password)`: This function takes in two parameters: `username` and `password`. It should search for a user with the given `username` in the `users` list and check if the corresponding `password` matches. If a matching user is found, print "Login successful!". Otherwise, print "Invalid username or password.".

3. `change_password(username, old_password, new_password)`: This function takes in three parameters: `username`, `old_password`, and `new_password`. It should find the user with the given `username` in the `users` list and check if the `old_password` matches. If it does, update the user's `password` with the `new_password` and print "Password changed successfully!". If the `old_password` doesn't match, print "Invalid password."
4. Add some other features of your choice\

## Hint:
- You can use args or kwargs or both \

- Use the following test cases:

```
register_user("john123", "pass123", "john@example.com")
register_user("emma456", "abc456", "emma@example.com")
register_user("james789", "xyz789", "james@example.com")

login_user("john123", "pass123")
login_user("emma456", "wrongpass")
login_user("james789", "xyz789")

change_password("john123", "pass123", "newpass")
change_password("emma456", "wrongpass", "newpass")
```

Expected output:

```
[{'username': 'john123', 'password': 'pass123', 'email': 'john@example.com'}, {'username': 'emma456', 'password': 'abc456', 'email': 'emma@example.com'}, {'username': 'james789', 'password': 'xyz789', 'email': 'james@example.com'}]
Login successful!
Invalid username or password.
Login successful!
Password changed successfully!
Invalid password.
```

Feel free to modify the exercise to suit your needs or add more functionality to the user registration system.
