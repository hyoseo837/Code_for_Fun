import tkinter
from tkinter.filedialog import askdirectory
root = tkinter.Tk()
root.withdraw()
filename = askdirectory(parent = root)

print(filename)