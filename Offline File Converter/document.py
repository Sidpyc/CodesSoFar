import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil

# Function to handle dropdown selection
def handle_selection():
    selected_format = file_format.get()
    print(f"Selected format: {selected_format}")

# Function to handle file upload
def upload_file():
    selected_format = file_format.get()
    filetypes = (
        (f"{selected_format} files", f"*.{selected_format.lower()}"),
    )
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path.endswith(f".{selected_format.lower()}"):
        print(f"Uploaded file path: {file_path}")
        # Update the label with the file name and path
        file_label.config(text=f"Uploaded File: {file_path}")
    else:
        print("Invalid file format selected.")

# Function to handle file conversion
def convert_file():
    selected_format = file_format2.get()
    original_path = file_label["text"][14:]
    base_path = "/".join(original_path.split("/")[:-1])
    file_name = original_path.split("/")[-1]
    converted_path = f"{base_path}/{file_name.split('.')[0]}.{selected_format.lower()}"
    print(f"Converted file path: {converted_path}")
    # Perform the file conversion and save the converted file to the original location
    # Here, we'll just copy the file to the converted path for demonstration purposes
    shutil.copy(original_path, converted_path)

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Document Flix")

# Set the window geometry
window.geometry("500x250")

# Set the background color
window.configure(bg="#ADD8E6")

# Create a dropdown box
file_format = tk.StringVar()
dropdown1 = ttk.Combobox(window, textvariable=file_format, values=["Text", "PDF"])
dropdown1.pack()

# Create an "Upload" button
upload_button = tk.Button(window, text="Upload", command=upload_file)
upload_button.pack()

# Create a label to display the file name and path
file_label = tk.Label(window, text="Uploaded File: ")
file_label.pack()

# Create a second dropdown box
file_format2 = tk.StringVar()
dropdown2 = ttk.Combobox(window, textvariable=file_format2, values=["Text", "PDF"])
dropdown2.pack()

# Create a "Convert" button
convert_button = tk.Button(window, text="Convert", command=convert_file)
convert_button.pack()

# Run the Tkinter event loop
window.mainloop()
