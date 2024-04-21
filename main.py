import tkinter as tk
import customtkinter as ctk
import functions as func


def main():
    root_tk = tk.Tk()
    root_tk.geometry("900x500")
    root_tk.title("Bouddha")
    
    bouton = ctk.CTkButton(master=root_tk, corner_radius=10, command=print(func.getFormat("books/books.json")), text="Upload", fg_color="navy")
    bouton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    root_tk.mainloop()
if __name__ == "__main__":
    main()
