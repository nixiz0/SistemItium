import tkinter as tk
from PIL import ImageTk, Image

from functions.center_interface import center_window
from functions.software_installer import installer_software
from functions.app_installer import installer_app
from functions.github_app_installer import installer_github_app


bg_color = '#333333'
fg_color = 'white'
font_size = 14
root = tk.Tk()
root.title("SistemItium")
root.configure(bg=bg_color)

logo = ImageTk.PhotoImage(Image.open("ressources/logo_sistemitium.png"))
logo_label = tk.Label(root, image=logo, bg=bg_color)
logo_label.pack(pady=10)

button1 = tk.Button(root, text="Install Softwares", command=installer_software, 
                    font=("Helvetica", font_size), bg=bg_color, fg=fg_color, width=14)
button1.pack(pady=10)

button2 = tk.Button(root, text="Initium Apps", command=installer_app, 
                    font=("Helvetica", font_size), bg=bg_color, fg=fg_color, width=14)
button2.pack(pady=10)

button3 = tk.Button(root, text="GitHub Apps", command=installer_github_app, 
                    font=("Helvetica", font_size), bg=bg_color, fg=fg_color, width=14)
button3.pack(pady=10)

root.minsize(230, 310)
root.maxsize(270, 350)

# Call the center_window function
center_window(root, 250, 330)
root.mainloop()