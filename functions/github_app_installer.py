import tkinter as tk
import webbrowser

from functions.center_interface import center_window


root = None
def installer_github_app():
    global root
    if root is not None:
        root.lift()
        root.deiconify()
        return
    
    apps_github = {
        "StableDiffusion": "https://github.com/lllyasviel/Fooocus",
        "NVIDIA Eye Tracker": "https://github.com/NVIDIA/MAXINE-AR-SDK",
        "AI Voice Changer": "https://github.com/w-okada/voice-changer",
    }

    root = tk.Toplevel()
    root.title("SistemItium GitHub Apps")
    root.configure(bg='#333333')

    title = tk.Label(root, text="Choose Apps to install", bg='#333333', fg='white', font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    for app, url in apps_github.items():
        button = tk.Button(root, text=app, command=lambda url=url: webbrowser.open(url), 
                           bg='#333333', fg='white', font=("Helvetica", 14), width=16)
        button.pack(side='top', padx=5, pady=5)
        
    root.minsize(330, 210)
    root.maxsize(370, 250) 
    center_window(root, 350, 230)