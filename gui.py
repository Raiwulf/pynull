import os
import re
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, Tk
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
FRAME0_PATH = ASSETS_PATH / "frame0"
FONT_FOLDER = ASSETS_PATH / "fonts"
ICON_FOLDER = ASSETS_PATH / "icons"
CONFIG_FILE = OUTPUT_PATH / "config.txt"

icon = ICON_FOLDER / "icon.ico"

def relative_to_assets(path: str) -> Path:
    return FRAME0_PATH / Path(path)

def open_file_dialog():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)

def process_files():
    directory_path = entry_path.get()
    regex_filter = entry_regex.get()
    backup_folder = os.path.join(directory_path, 'pyNull_Backups')

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    try:
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                if re.search(regex_filter, filename):
                    source_file = os.path.join(root, filename)
                    backup_file = os.path.join(backup_folder, filename)

                    if source_file != backup_file:
                        shutil.copy(source_file, backup_file)

                        open(source_file, 'w').close()

        entry_log.config(state=tk.NORMAL)
        entry_log.insert(tk.END, "Files nulled successfully!\n")
        entry_log.config(state=tk.DISABLED)
    except Exception as e:
        entry_log.config(state=tk.NORMAL)
        entry_log.insert(tk.END, f"Error: {str(e)}\n")
        entry_log.config(state=tk.DISABLED)

def save_data():
    with open(CONFIG_FILE, "w") as file:
        file.write(f"{entry_path.get()}\n")
        file.write(f"{entry_regex.get()}\n")

def load_data():
    try:
        with open(CONFIG_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                entry_path.delete(0, tk.END)
                entry_path.insert(0, lines[0].strip())
                entry_regex.delete(0, tk.END)
                entry_regex.insert(0, lines[1].strip())
    except FileNotFoundError:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, "Path")
        entry_regex.delete(0, tk.END)
        entry_regex.insert(0, "RegEx")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
        save_data()
        window.destroy()

window = Tk()

window.geometry("375x512")
window.configure(bg = "#FFFFFF")
window.title("CigiLabs - pyNull")
window.iconbitmap(icon)
custom_font = FONT_FOLDER / "Comfortaa-Regular.ttf"
window.option_add("*Font", custom_font)
window.protocol("WM_DELETE_WINDOW", on_closing)


canvas = Canvas(
    window,
    bg = "#d9d9d9",
    height = 512,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    187.0,
    256.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    105.0,
    image=image_image_2
)

button_process_image = PhotoImage(
    file=relative_to_assets("button_process.png"))
button_process = Button(
    image=button_process_image,
    borderwidth=0,
    highlightthickness=0,
    command=process_files,
    relief="flat"
)
button_process.place(
    x=32.0,
    y=336.0,
    width=315.0,
    height=58.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    217.0,
    315.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    217.0,
    221.0,
    image=image_image_4
)

entry_regex_image = PhotoImage(
    file=relative_to_assets("entry_regex.png"))
entry_regex_bg = canvas.create_image(
    217.5,
    284.0,
    image=entry_regex_image
)
entry_regex = Entry(
    bd=0,
    bg="#d9d9d9",
    fg="#000716",
    highlightthickness=0
)
entry_regex.place(
    x=96.0,
    y=260.0,
    width=243.0,
    height=46.0
)

entry_path_image = PhotoImage(
    file=relative_to_assets("entry_path.png"))
entry_path_bg = canvas.create_image(
    217.5,
    190.0,
    image=entry_path_image
)
entry_path = Entry(
    bd=0,
    bg="#d9d9d9",
    fg="#000716",
    highlightthickness=0
)
entry_path.place(
    x=96.0,
    y=166.0,
    width=243.0,
    height=46.0
)

entry_log_image = PhotoImage(
    file=relative_to_assets("entry_log.png"))
entry_log_bg = canvas.create_image(
    189.5,
    456.5,
    image=entry_log_image
)
entry_log = Text(
    bd=0,
    bg="#d9d9d9",
    fg="#000716",
    highlightthickness=0
)
entry_log.place(
    x=40.0,
    y=414.0,
    width=299.0,
    height=83.0
)
entry_log.config(state=tk.DISABLED)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    56.0,
    284.0,
    image=image_image_5
)

button_folder_image = PhotoImage(
    file=relative_to_assets("button_folder.png"))
button_folder = Button(
    image=button_folder_image,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_dialog,
    relief="flat"
)
button_folder.place(
    x=32.0,
    y=166.0,
    width=48.0,
    height=48.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    217.0,
    110.0,
    image=image_image_6
)

canvas.create_text(
    38.0,
    192.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Comfortaa Bold", 16 * -1)
)

def open_github_url():
    webbrowser.open_new("https://github.com/Raiwulf/pynull")

about_button = tk.Button(
    window,
    text="Info",
    command=open_github_url,
    padx=8,
    pady=4,
)
about_button.pack(side="top", anchor="ne")

load_data()

window.resizable(False, False)
window.mainloop()
