from tkinter import*
root=Tk()

root.geometry("400x400")


menu_bar=Menu(root)
root.config(menu=menu_bar)

file=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save As")
file.add_command(label="Save")

edit=Menu(menu_bar,tearoff=1)
menu_bar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo")
edit.add_command(label="Redo")
edit.add_separator()
edit.add_command(label="Copy")
edit.add_command(label="Cut")
edit.add_command(label="Paste")


root.mainloop()
