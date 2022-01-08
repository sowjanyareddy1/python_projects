# we need to first download the library
# This is to understand the basic validator concept
# the hashed password is actually in db in real time.
import bcrypt
# convert password into bytes
password = b"thisismypassword"
# now use the function hashpw and also gensalt() method
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# accept password from user to login
user_password = input("Enter the password: ")
user_password = bytes(user_password, encoding='utf-8')
# this checkpw is used to check if both are same
if(bcrypt.checkpw(user_password, hashed)):
    print("password matches")
else:
    print("invalid password")