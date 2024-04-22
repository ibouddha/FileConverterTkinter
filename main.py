import tkinter as tk
import customtkinter as ctk
from CTkTable import *
import functions as func  # importons les fonctions BackEnd


def get_selected_file():
    """Opens a file dialog and returns the selected file path."""
    filename = tk.filedialog.askopenfilename(
        title="Select File",
        filetypes=[("All Files", "*.*")]  # Allow all file types by default
    )
    return filename


def display_content(text_widget, filename):
    """Displays the selected file content in the text widget."""
    if not filename:
        text_widget.delete("1.0", tk.END)  # Clear the displayer if no file chosen
        return

    try:
        # Assuming func.getFormat returns the content as a string
        content = func.read(filename)
        text_widget.delete("1.0", tk.END)  # Clear the displayer before writing
        text_widget.insert("1.0", content)
    except Exception as e:
        print(f"Error displaying content: {e}")
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "Error processing file.")


def main():
    root_tk = tk.Tk()
    root_tk.geometry("900x1500")
    root_tk.title("Bouddha")

    # File uploader button
    upload_button = ctk.CTkButton(
        master=root_tk,
        corner_radius=10,
        text="Upload",
        fg_color="navy",
        command=lambda: upload_file(root_tk)  # Pass root_tk for disabling after upload
    )
    upload_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Displayer (text widget)
    text_display = tk.Text(root_tk, font=("Arial", 12), wrap=tk.WORD, width=80)  # Adjust width as needed
    text_display.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.4, anchor=tk.CENTER)
    
    json_button = ctk.CTkButton(
        master=root_tk,
        corner_radius=10,
        text="Json",
        fg_color="navy",
        command=lambda: func.csvtojson()  # Pass root_tk for disabling after upload
    )
    csv_button = ctk.CTkButton(
        master=root_tk,
        corner_radius=10,
        text="Json",
        fg_color="navy",
        command=lambda: func.csvtojson()  # Pass root_tk for disabling after upload
    )
    xml_button = ctk.CTkButton(
        master=root_tk,
        corner_radius=10,
        text="Json",
        fg_color="navy",
        command=lambda: func.csvtojson()  # Pass root_tk for disabling after upload
    )
    
    json_button.place(relwidth=0.1,relx=0.4,rely=0.6, anchor=tk.CENTER)

    def upload_file(window):
        """Handles file upload, disables button, and displays content."""
        selected_file = get_selected_file()
        if selected_file:
            # Process the selected file (call func.getFormat, etc.)
            display_content(text_display, selected_file)
            upload_button.configure(state=tk.DISABLED)  # Disable button after upload
            

    root_tk.mainloop()


if __name__ == "__main__":
    main()
