from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from model import Model

class CarsApp:

    def __init__(self, root):
        self.root = root
        self.root.title('Учет проезда автомобилей')
        self.model = Model()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_reqwidth() - 150) // 2
        y = (screen_height - self.root.winfo_reqheight() - 150) // 2
        self.root.geometry(f"+{x}+{y}")
        
        main_frame = ttk.Frame(self.root, padding='10')
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.table_cars = ttk.Treeview(main_frame, columns=('car_type', 'date', 'time', 'plate'), show='headings')
        self.table_cars.heading('car_type', text='Тип')
        self.table_cars.heading('date', text='Дата')
        self.table_cars.heading('time', text='Время')
        self.table_cars.heading('plate', text='Номер')
        self.table_cars.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        add_button = ttk.Button(button_frame,text='Добавить',command=self.create_add_car_menu)
        add_button.pack(side=tk.LEFT, padx=5)

        remove_button = ttk.Button(button_frame, text='Удалить',command=self.remove_car)
        remove_button.pack(side=tk.LEFT, padx=5)

        load_button = ttk.Button(button_frame, text='Загрузить',command=self.load_car)
        load_button.pack(side=tk.LEFT, padx=5)

        save_button = ttk.Button(button_frame, text='Сохранить',command=self.save_car)
        save_button.pack(side=tk.LEFT, padx=5)

    def update(self):
        for row in self.table_cars.get_children():
            self.table_cars.delete(row)

        for car in self.model.get_all_cars():
            print(car.to_array())
            self.table_cars.insert('', tk.END, values=car.to_array())
            

    def create_add_car_menu(self):
        create_window = tk.Toplevel(self.root)
        create_window.title('Добавить авто')
        screen_width = create_window.winfo_screenwidth()
        screen_height = create_window.winfo_screenheight()
        x = (screen_width - create_window.winfo_reqwidth()) // 2
        y = (screen_height - create_window.winfo_reqheight()) // 2
        create_window.geometry(f"+{x}+{y}")

        ttk.Label(create_window, text='Тип авто:').grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        car_type_combobox = ttk.Combobox(create_window, values=['passenger', 'truck'])
        car_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(create_window, text='Номер авто:').grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        car_number_entry = ttk.Entry(create_window)
        car_number_entry.grid(row=1, column=1, padx=5, pady=5)
        car_number_entry.insert(0, "А123АА123")

        ttk.Label(create_window, text='Дата:').grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        date_entry = ttk.Entry(create_window)
        date_entry.grid(row=2, column=1, padx=5, pady=5)
        date_entry.insert(0, datetime.now().strftime('%d.%m.%Y'))

        ttk.Label(create_window, text='Время:').grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        time_entry = ttk.Entry(create_window)
        time_entry.grid(row=3, column=1, padx=5, pady=5)
        time_entry.insert(0, datetime.now().strftime('%H:%M'))

        button_frame = ttk.Frame(create_window)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame,text='Добавить', command=lambda: self.add_car(car_type_combobox.get(), car_number_entry.get(), date_entry.get(), time_entry.get(), create_window)).pack(side=tk.LEFT, padx=5)
    
    def save_car(self):
        self.model.save_to_file('1.txt')
        messagebox.showinfo('info', 'Сохранены данные в файл')
    
    def load_car(self):
        self.model.load_from_file('1.txt')
        print(self.model.get_all_cars())
        self.update()
        
        messagebox.showinfo('info', 'Загружены данные с файла')

    def add_car(self, type, car_number, date_str, time_str, dialog):
        try:
            assert type != '', 'Некорректные данные'
            dt = datetime.strptime(f'{date_str} {time_str}', '%d.%m.%Y %H:%M')
            self.model.add_car(type, car_number, dt)
            self.update()
            dialog.destroy()
        except:
            messagebox.showerror('Ошибка', f'Некорректные данные')

    def remove_car(self):
        selected_item = self.table_cars.selection()
        if selected_item:
            index = self.table_cars.index(selected_item[0])
            self.model.remove_car(index)
            self.update()
