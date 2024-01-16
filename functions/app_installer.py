import tkinter as tk
import webbrowser

from functions.center_interface import center_window


root = None
def installer_app():
    global root
    if root is not None:
        root.lift()
        root.deiconify()
        return
    
    apps = {
        "Curatio": "https://github.com/nixiz0/Curatio-App",
        "Agentis": "https://github.com/nixiz0/Agentis",
        "Loqui": "https://github.com/nixiz0/Loqui",
        "Agnitium": "https://github.com/nixiz0/Agnitium",
        "Virtualis": "https://github.com/nixiz0/Virtualis",
        "DrawItium": "https://github.com/nixiz0/DrawItium",
    }

    root = tk.Toplevel()
    root.title("SistemItium Initium Apps")
    root.configure(bg='#333333')

    title = tk.Label(root, text="Choose Apps to install", bg='#333333', fg='white', font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    for app, url in apps.items():
        button = tk.Button(root, text=app, command=lambda url=url: webbrowser.open(url), 
                           bg='#333333', fg='white', font=("Helvetica", 14), width=16)
        button.pack(side='top', padx=5, pady=5)
        
    root.minsize(330, 405)
    root.maxsize(370, 420) 
    center_window(root, 350, 410)