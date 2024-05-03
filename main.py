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


# Main function
def main():
    root_tk = tk.Tk()
    root_tk.geometry("400x500")
    root_tk.title("Bouddha")

    # File uploader button
    upload_button = ctk.CTkButton(
        master=root_tk,
        corner_radius=10,
        text="Upload",
        fg_color="navy",
        command=lambda: upload_file()  # Pass root_tk for disabling after upload
    )
    upload_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Displayer (text widget)
    text_display = tk.Text(root_tk, font=("Arial", 12), wrap=tk.WORD, width=80)  # Adjust width as needed
    text_display.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.4, anchor=tk.CENTER)

    options = ["default", "csvtojson", "csvtoxml", "csvtoyaml", "jsontocsv", "jsontoxml", "jsontoyaml", "xmltojson",
               "xmltocsv", "xmltoyaml"]

    selected_option = tk.StringVar()
    selected_option.set(options[0])

    option_menu = tk.OptionMenu(
        root_tk,  # Pass parent window as keyword argument
        selected_option,
        *options
    )
    option_menu.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # ... (Rest of your code)

    def on_option_change():
        option_functions = {
            "default": "",
            "csvtojson": print(func.csvtojson(get_selected_file())),
            "csvtoxml": print(func.csvtoxml(get_selected_file())),
            "csvtoyaml": print(func.csvtoyaml(get_selected_file())),
            "jsontoxml": print(func.jsontoxml(get_selected_file())),
            "jsontocsv": print(func.jsontocsv(get_selected_file())),
            "jsontoyaml": print(func.jsontoyaml(get_selected_file())),
            "xmltocsv": print(func.xmltocsv(get_selected_file())),
            "xmltojson": print(func.xmltojson(get_selected_file())),
            "xmltoyaml": print(func.xmltoyaml(get_selected_file())),
            "yamltocsv": print(func.xmltoyaml(get_selected_file())),
            "yamltojson": print(func.xmltoyaml(get_selected_file())),
            "yamltoxml": print(func.xmltoyaml(get_selected_file())),
            # ... Add more options and functions here
        }

        selected_option.trace_add("write", on_option_change)

        selected_option_value = selected_option.get()
        if selected_option_value in option_functions:
            option_functions[selected_option_value]()  # Call the function for the selected option
            print(selected_option_value)

    def upload_file():
        """Handles file upload, disables button, and displays content."""
        selected_file = get_selected_file()
        if selected_file:
            # Process the selected file (call func.getFormat, etc.)
            display_content(text_display, selected_file)

    root_tk.mainloop()


if __name__ == "__main__":
    main()
