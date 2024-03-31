import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import ttk

class History_list:
    def __init__(self, root):
        self.root = root
        self.root.title("History Record List")
        self.create_table()
        self.create_record_ui()
        self.show_records()

    def create_table(self):
        # Create a table in the database if it doesn't exist
        conn = sqlite3.connect('Record.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS records
                    (id INTEGER PRIMARY KEY, 
                    time DATE,
                    record TEXT 
                    )'''
                    )
        conn.commit()
        cursor.close()
        conn.close()

    def create_record_ui(self):
        self.tree = ttk.Treeview(self.root, columns=('Time', 'Record Contents'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Time')
        self.tree.heading('#2', text='Record Contents')
        self.tree.pack()

        #self.text_enter = tk.Entry(self.root, width=30)
        #self.text_enter.pack()
        #self.add_button = tk.Button(self.root, text="Add Record", command=self.add_record_click)
        #self.add_button.pack()
        self.delete_button = tk.Button(self.root, text="Delete Record", command=self.delete_selected_record)
        self.delete_button.pack()

    def add_record(self, text):
        # Add a new record to the database
        conn = sqlite3.connect('Record.db')
        cursor = conn.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO records (time, record) VALUES (?, ?)", (current_time, text))
        conn.commit()
        cursor.close()
        conn.close()

        self.show_records()

    def show_records(self):
        # Show records in the Treeview
        conn = sqlite3.connect('Record.db')
        cursor = conn.cursor()
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor.execute("SELECT * FROM records")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert('', 'end', text=row[0], values=(row[1], row[2]))
        cursor.close()
        conn.close()

    def delete_record(self, record_id):
        # Delete a record from the database
        conn = sqlite3.connect('Record.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
        conn.commit()
        cursor.close()
        conn.close()

        self.show_records()

    def delete_selected_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            record_id = self.tree.item(selected_item)['text']
            self.delete_record(record_id)
        else:
            tk.messagebox.showinfo("Error", "Can not delect")

    #Add record using button
    def add_record_click(self):
        # Get text from the textbox
        text = self.text_enter.get()
        if text:
            self.add_record(text)
            self.text_enter.delete(0, tk.END)
        else:
            tk.messagebox.showinfo("Error", "Please enter text")
    

root = tk.Tk()
ob = History_list(root)
root.mainloop()
