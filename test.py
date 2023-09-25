from tkinter import Tk, Button, Label

current_theme = "light"


def change_theme():
    current_bg = root.cget("bg")
    new_theme = "light" if current_theme == "dark" else "dark"
    theme_colors = themes[new_theme]
    root.configure(bg=theme_colors["bg"])
    change_theme_button.configure(bg=theme_colors["button"], fg=theme_colors["text"])
    info_label.configure(bg=theme_colors["bg"], fg=theme_colors["text"])
    global current_theme
    current_theme = new_theme


themes = {
    "light": {"bg": "white", "button": "lightgrey", "text": "black"},
    "dark": {"bg": "black", "button": "grey", "text": "white"},
}


root = Tk()
root.geometry("300x300")
root.title("Advanced Theme Changer")

info_label = Label(root, text="Click the button to change the theme")
info_label.pack(pady=10)

change_theme_button = Button(root, text="Change Theme", command=change_theme)
change_theme_button.pack()

root.mainloop()
