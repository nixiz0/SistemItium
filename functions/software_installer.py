import tkinter as tk
import webbrowser
from tkinter import messagebox

from functions.center_interface import center_window


root = None
def installer_software():
    global root
    if root is not None:
        if root.winfo_exists():
            root.lift()
            root.deiconify()
            return
        else:
            root = None
    
    software = {
        "Python 3.11": "https://www.python.org/downloads/release/python-3117/",
        "Git": "https://git-scm.com/downloads",
        "VSCode": "https://code.visualstudio.com/download",
        "VSCode C++": "https://visualstudio.microsoft.com/fr/vs/features/cplusplus/",
        "OBS": "https://obsproject.com/fr/download",
        "Discord": "https://discord.com/download",
        "Google Chrome": "https://www.google.com/chrome/",
        "Libre Office": "https://www.libreoffice.org/download/download/",
        "CoreTemp": "https://www.alcpu.com/CoreTemp/",
        "Ubuntu": "https://ubuntu.com/download/desktop",
        "Arduino": "https://www.arduino.cc/en/software",
        "NVidia": "https://www.nvidia.com/fr-fr/geforce/geforce-experience/download/",
        "Java": "https://www.java.com/fr/download/manual.jsp",
        "VLC": "https://www.videolan.org/vlc/index.fr.html",
        "TablePlus": "https://tableplus.com/download",
        "LetsView": "https://letsview.com/fr/download-letsview",
    }
    
    def submit():
        selected_apps = [app for app, button in buttons.items() if button.cget('fg') == 'white']
        if not selected_apps:
            messagebox.showerror("Error", "Please select at least one app before submitting.")
            return
        messagebox.showinfo("Installing Applications", "The following applications will be installed:\n" + "\n".join(selected_apps))
        for app in selected_apps:
            webbrowser.open(software[app])

    def toggle(button):
        if button.cget('fg') == 'gray':
            button.config(fg='white')
        else:
            button.config(fg='gray')

    root = tk.Toplevel()
    root.title("SistemItium Softwares")
    root.configure(bg='#333333')

    title = tk.Label(root, text="Choose Softwares to install", bg='#333333', fg='white', font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    buttons = {}
    app_list = list(software.keys())
    for i in range(0, len(app_list), 2):
        frame = tk.Frame(root, bg='#333333')
        frame.pack(pady=5)
        for j in range(2):
            if i + j < len(app_list):
                app = app_list[i + j]
                button = tk.Button(frame, text=app, command=lambda app=app: toggle(buttons[app]), 
                                   bg='#333333', fg='gray', font=("Helvetica", 12), width=13)
                buttons[app] = button
                button.pack(side='left', padx=5)

    submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
    submit_button.pack(pady=10)
    
    root.minsize(330, 440)
    root.maxsize(370, 460) 
    center_window(root, 350, 450)