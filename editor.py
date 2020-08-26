import tkinter as tk
from tkinter import *
from settings import *

app = tk.Tk()

app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGHT)
app.geometry(f'{WIDTH}x{HEIGHT}+200+100')

text = tk.Text(app, width=WIDTH-50, height=HEIGHT, wrap='word')
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)
scroll.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll.set)
text.pack()

menu_bar = tk.Menu(app)

editor = TextEditor(text)

# выпадающее меню вкладки 'Файл'
app_menu = tk.Menu(menu_bar)
app_menu.add_command(label='Новый файл', command=editor.new_file)
app_menu.add_command(label='Открыть файл', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

# выпадающее меню вкладки 'Справка'
ref_menu = tk.Menu(menu_bar)
ref_menu.add_command(label='Документация', command=editor.get_info_doc)
ref_menu.add_command(label='О программе', command=editor.get_info)

# основные вкладки меню
menu_bar.add_cascade(label='Файл', menu=app_menu)
menu_bar.add_cascade(label='Справка', menu=ref_menu)
menu_bar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menu_bar)
app.mainloop()
