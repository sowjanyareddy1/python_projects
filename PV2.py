# we are validating only using the hash value

from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$AzSaPOn0uhliwZmJbMgl8.dGqdzkIeS5nI2uDeGi5wy706bKoHb8.'
    password = bytes(password, encoding='utf-8')
    if(bcrypt.checkpw(password, hash)):
        print("password matches")
    else:
        print("invalid password")

root = Tk()
# window size
root.geometry("300x300")

# a entry to get password from user
user_pass = Entry(root)
user_pass.pack()
button = Button(text="Validate", 
                command=lambda: validate(user_pass.get()))

button.pack()

root.mainloop()