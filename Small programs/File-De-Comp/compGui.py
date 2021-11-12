import tkinter as tk
from compressv2 import compress,decompress

def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label1 =tk.Label(window, text = 'File to de/compress')
output_label1 =tk.Label(window, text = 'De/Compressed file')

compress_button = tk.Button(window, text = 'Compress', command= lambda:compression(input_entry.get(), output_entry.get()) )
decompress_button = tk.Button(window, text= 'Decompress', command= lambda:decompression(input_entry.get(),output_entry.get()))

input_label1.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
output_label1.grid(row=1, column=0)
output_entry.grid(row=1, column=1)
compress_button.grid(row=2,column=1)
decompress_button.grid(row=2,column=2)
window.mainloop()
