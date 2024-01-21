import tkinter as tk
from tkinter import ttk
from config import load_env
from beginApplys import BeginApply


class AppGUI:
    def __init__(self):
        self.ba = BeginApply()
        self.bg = "#e0e0e0"
        self.window = tk.Tk()
        self.window.title("Apply Bot")
        self.window.resizable(False, False)
        self.window.configure(bg=self.bg)

        # Crear etiquetas y entradas
        self.tag_name = self.crear_label("Name:")
        self.entry_name = self.crear_entry()

        self.tag_lastname = self.crear_label("Lastname:")
        self.entry_lastname = self.crear_entry()

        self.tag_email = self.crear_label("Email:")
        self.entry_email = self.crear_entry()

        self.tag_password = self.crear_label("Password:")
        self.entry_password = self.crear_entry(show="*")

        self.tag_positions = self.crear_label("Position:")
        self.entry_positions = self.crear_entry()

        self.tag_sites = self.crear_label("Select a web:")
        self.options = ["Linkedin", "Indeed"]
        self.entry_sites = ttk.Combobox(self.window, values=self.options)

        # Botón para obtener los datos
        self.boton = tk.Button(
            self.window, text="Start Bot", command=self.makeEnv, height=2, width=50
        )

        # Organizar en la cuadrícula
        self.tag_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.tag_lastname.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.entry_lastname.grid(row=0, column=3, padx=10, pady=10)

        self.tag_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.tag_password.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.entry_password.grid(row=1, column=3, padx=10, pady=10)

        self.tag_positions.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_positions.grid(row=2, column=1, padx=10, pady=10)

        self.tag_sites.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.entry_sites.grid(row=2, column=3, padx=10, pady=10)

        self.boton.grid(row=3, column=0, columnspan=4, pady=10)

        self.getEnv()

    def getEnv(self):
        self.env = load_env({})

        if self.env:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, self.env["NAME"])

            self.entry_lastname.delete(0, tk.END)
            self.entry_lastname.insert(0, self.env["LASTNAME"])

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, self.env["EMAIL"])

            self.entry_password.delete(0, tk.END)
            self.entry_password.insert(0, self.env["PASSWORD"])

            self.entry_positions.delete(0, tk.END)
            self.entry_positions.insert(0, self.env["POSITIONS"][0])

            self.entry_sites.delete(0, tk.END)
            self.entry_sites.insert(0, self.env["SITES"][0])

    def makeEnv(self):
        data = self.obtener_datos()
        self.env = load_env(data)
        self.ba.makeApplications(self.env)

    def obtener_datos(self):
        data = {
            "NAME": self.entry_name.get(),
            "LASTNAME": self.entry_lastname.get(),
            "PASSWORD": self.entry_password.get(),
            "EMAIL": self.entry_email.get(),
            "POSITIONS": [self.entry_positions.get()],
            "SITES": [self.entry_sites.get()],
        }
        return data

    def crear_label(self, text):
        return tk.Label(self.window, text=text, bg=self.bg)

    def crear_entry(self, show=None):
        return tk.Entry(self.window, show=show)

    def startApp(self):
        self.window.mainloop()
