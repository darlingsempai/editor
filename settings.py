import codecs
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename #функции как открыть и закрыть файл
from tkinter.messagebox import showerror # показ всех ошибок
from tkinter import messagebox # уведомления приложения

APP_NAME = 'World Web Write'

WIDTH = 1000
HEIGHT = 650

class TextEditor:
    def __init__(self, text):
        self.file_name = tk.NONE
        self.text = text

    def new_file(self):
        self.file_name = 'Без названия'
        self.text.delete('1.0', tk.END)

    def open_file(self):
        inp = askopenfilename()
        with codecs.open(inp, 'r', encoding='utf-8') as f:
            data = f.read()
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', data)

    def save_file(self):
        data = self.text.get('1.0', tk.END)
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(data)

    def save_as_file(self):
        data = self.text.get('1.0', tk.END)
        output = asksaveasfilename(defaultextension='txt')
        try:
            with open(output, 'w', encoding='utf8') as f:
                f.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!', message='Ошибка при сохранении файла :(')

    def get_info(self):
        messagebox.showinfo('Справка', 'Приложение разработано компанией Google')

    def get_info_doc(self):
        messagebox.showinfo('Документация', 'С помощью нашего приложения вы можете делать записи и сохранять их')
