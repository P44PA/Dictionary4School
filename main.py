import json
import tkinter as tk
from tkinter import messagebox
from difflib import get_close_matches
from tkinter import ttk

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Dictionary App")
        master.geometry("510x600")  # Set a fixed-size window
        master.configure(bg="#fe9e1a")

        # Header
        self.header_label = tk.Label(master, text="Dictionary App", font=("Helvetica", 18, "bold"), bg="#fe9e1a")
        self.header_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry with Placeholder
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(master, font=("Helvetica", 14), justify="left", width=35, textvariable=self.entry_var)
        self.entry.grid(row=1, column=0, padx=10, pady=10, ipady=5, sticky="w")
        self.entry_var.set("Enter a word...")  # Placeholder text
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)

        # Lookup Button
        self.lookup_button = tk.Button(master, text="Search", command=self.translate, font=("Helvetica", 14), bg="#f86f03", fg="white")
        self.lookup_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Result Label with Default Image
        self.default_image_path = "./dict1.png"  # Replace with your image path
        self.default_image = tk.PhotoImage(file=self.default_image_path)
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(master, textvariable=self.result_text, font=("Helvetica", 14), wraplength=380, justify="left", bg="#f8f9fc", image=self.default_image, compound="top")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def clear_placeholder(self, event):
        if self.entry_var.get() == "Enter a word...":
            self.entry_var.set("")

    def restore_placeholder(self, event):
        if not self.entry_var.get():
            self.entry_var.set("Enter a word...")

    def translate(self):
        word = self.entry.get().lower()
        output = self.lookup_word(word)

        if output is None:
            # Display default image when there is no text
            self.result_text.set("")
            self.result_label.config(image=self.default_image)
        else:
            if isinstance(output, list):
                result = "\n".join(output)
            else:
                result = output

            self.result_text.set(result)
            self.result_label.config(image="")  # Remove the image if there is text

    def lookup_word(self, w):
        if w in data:
            return data[w]
        elif close_matches := get_close_matches(w, data.keys()):
            suggested_word = close_matches[0]
            confirmation = messagebox.askquestion("Did you mean?", f'Did you mean "{suggested_word}"?')

            if confirmation == "yes":
                return data[suggested_word]
            else:
                return "Word not found. Please check the spelling."
        else:
            return None  # Returning None to indicate no result

if __name__ == "__main__":
    # Load the data
    with open("./package.json", "r") as file:
        data = json.load(file)

    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
