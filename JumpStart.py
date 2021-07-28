import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
"""
A tkinter GUI desktop application
an app that Jumpstarts your day by launching assigned frequently used apps or files 
"""
# tkinter GUI initialization
root = tk.Tk()
root.title("Jump Start")
icon = PhotoImage(file='JS.png')
root.iconphoto(False, icon)

launch_files = []  # a list to hold files/apps path
file_name = set()  # a set to hold the file/app name

# if a preference list (.txt) of files/apps to launch exists, recall lists
if os.path.isfile('preference.txt'):
    with open('preference.txt', 'r') as f:
        saved_files = f.read()
        saved_files = saved_files.split(",")
        launch_files = [x for x in saved_files if x.strip()]

        for i in launch_files:
            j = i.split("/")
            file_name.add(j[-1])


def uploader():
    """
    Function called when the upload button is clicked. activates the open file dialogue
    saves each uploaded file/app path into a list
    :return: None
    """
    # clears the display board for every file/app upload
    # because the file label packs every item in the launch_files list at every click
    for widget in display_board.winfo_children():
        widget.destroy()

    # opens the file dialog, also sets the type of file accessible
    file_upload = filedialog.askopenfilename(initialdir="/", title="Upload App",
                                             filetypes=(("Application", "*.exe"), ("All Files", "*.*")))
    # saves every uploaded file/app path into list
    launch_files.append(file_upload)

    # iterate through the file paths to get the file/app name at the end of the path
    for i in launch_files:
        j = i.split("/")
        file_name.add(j[-1])

    # displays only the file/app name and not the path
    for name in file_name:
        file_label = tk.Label(display_board, text=name)
        file_label.pack()


def launcher():
    """
    Function to launch every files/apps uploaded into jumpstart
    :return: None
    """
    for files in launch_files:
        os.startfile(files)


def clear():
    """
    Clears the preference list of files/apps already uploaded to jumpstart
    :return: None
    """
    for widget in display_board.winfo_children():
        widget.destroy()

    launch_files.clear()
    file_name.clear()


"""Setting the application canvas and required buttons
also indicating which function to run at the click of a button"""
# application background
canvas = tk.Canvas(root, height=600, width=500, bg="#512C68")
canvas.create_text(250, 40, text="Files/Apps Launcher", fill="white", font=("Segoe 20 bold"))
canvas.pack()

# display view
display_board = tk.Frame(root, bg="white")
display_board.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1)

# upload file button
upload = tk.Button(root, text="Upload File", height=2, width=10,
                   padx=10, pady=3, bg="white", command=uploader)
upload.place(relx=0.2, rely=0.7)

# launch file button
run = tk.Button(root, text="Jump Start", height=2, width=10,
                padx=10, pady=3, bg="white", command=launcher)
run.place(relx=0.62, rely=0.7)

# clear queue button
reset = tk.Button(root, text="Clear Queue", height=2, width=40,
                  padx=10, pady=3, bg="#FF2812", fg="white", command=clear)
reset.place(relx=0.2, rely=0.8)


def run():
    """
    The run function to run the application in a loop
    while also displaying already saved preferences at launch
    :return:
    """
    # display from already saved preference
    for item in file_name:
        label = tk.Label(display_board, text=item)
        label.pack()

    # runs application in a loop
    root.mainloop()

    # saves/writes preferences into file
    with open('preference.txt', 'w') as f:
        for app in launch_files:
            f.write(app + ',')


if __name__ == "__main__":
    run()
