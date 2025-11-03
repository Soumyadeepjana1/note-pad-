import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, askyesno

def new_note(): txt.delete("1.0", tk.END); root.title("Untitled - Notepad")
def open_file():
    f = askopenfilename(filetypes=[("Text Files","*.txt")])
    if f: txt.delete("1.0", tk.END); txt.insert(tk.END, open(f,"r",encoding="utf-8").read()); root.title(f"{f} - Notepad")
def save_file():
    f = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if f: open(f,"w",encoding="utf-8").write(txt.get("1.0",tk.END)); root.title(f"{f} - Notepad"); showinfo("Saved","File saved successfully")
def delete_all(): txt.delete("1.0", tk.END)
def about(): showinfo("About","Simple Notepad by Soumyadeep")
def exit_app(): askyesno("Exit","Do you want to exit?") and root.destroy()

root = tk.Tk(); root.title("Notepad"); root.geometry("600x400")
txt = tk.Text(root,font=("Arial",12)); txt.pack(expand=True,fill="both")

menu = tk.Menu(root); root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=new_note)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Delete All", command=delete_all)
menu.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=help_menu)

root.mainloop()
