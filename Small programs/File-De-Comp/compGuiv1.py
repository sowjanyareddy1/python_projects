import tkinter as tk
from compressv2 import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file")
    return filename
def save_file():
    filename = filedialog.asksaveasfile(initialfile='Untitled.txt', defaultextension= '.txt', filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


compress_button = tk.Button(window, text = 'Compress', command= lambda:compression(open_file(), save_file()) )
decompress_button = tk.Button(window, text= 'Decompress', command= lambda:decompression(open_file(), save_file()))


compress_button.grid(row=2,column=1)
decompress_button.grid(row=2,column=2)
window.mainloop()
