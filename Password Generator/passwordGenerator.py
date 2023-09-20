import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.characterList = ""
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Password Generator")
        self.root.configure(bg="#0F2C59")
        
        self.title_label = tk.Label(self.root, text="Password Generator", font=('calibre', 26, 'bold'), fg="#DAC0A3", bg="#0F2C59")
        self.title_label.pack()

        self.pass_length = tk.IntVar()
        self.pass_complexity = tk.StringVar()
        self.password = []

        self.pass_length_label = tk.Label(self.root, text='Length', font=('calibre', 20, 'bold'), fg="#DAC0A3", bg="#0F2C59")
        self.pass_length_label.place(x=150, y=80)

        self.pass_length_entry = tk.Entry(self.root, font=('calibre', 16, 'normal'), bg="#F8F0E5")
        self.pass_length_entry.place(x=260, y=88)

        self.complexity_label = tk.Label(self.root, text='Complexity', font=('calibre', 20, 'bold'), fg="#DAC0A3", bg="#0F2C59")
        self.complexity_label.place(x=150, y=150)
        self.complexity_listbox = tk.Listbox(self.root, height=3, width=11, bg="#F8F0E5", font=('calibre', 16, 'bold'), fg="#0F2C59")
        self.complexity_listbox.insert(1, "1- Complex")
        self.complexity_listbox.insert(2, "2- Medium")
        self.complexity_listbox.insert(3, "3- Simple")
        self.complexity_listbox.place(x=320, y=130)

        self.generate_button = tk.Button(self.root, text="Generate", width=10, height=1, bg="#F8F0E5", font=('calibre', 16, 'bold'), fg="#0F2C59", command=self.generatePassword)
        self.generate_button.place(y=240, x=240)

        self.generated_password = tk.Label(self.root, text="", font=('calibre', 16, 'bold'), fg="#DAC0A3", bg="#0F2C59")
        self.generated_password.place(x=190, y=290)

    def generatePassword(self):
        self.characterList = ""
        self.password = []
        pass_length = int(self.pass_length_entry.get())
        pass_complexity = self.complexity_listbox.get(tk.ANCHOR)

        if pass_complexity == '1- Complex':
            self.characterList += string.ascii_letters + string.digits + string.punctuation
        elif pass_complexity == '2- Medium':
            self.characterList += string.ascii_letters + string.digits
        elif pass_complexity == '3- Simple':
            self.characterList += string.digits

        for _ in range(pass_length):
            randomchar = random.choice(self.characterList)
            self.password.append(randomchar)

        self.generated_password.configure(text=f'Generated password:\n {"".join(self.password)}')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
