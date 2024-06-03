import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

def fetch_data():
    try:
        conn = psycopg2.connect(
            dbname="shops",
            user="postgres",
            password="1111",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, url, image FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []

def update_table():
    for row in tree.get_children():
        tree.delete(row)
    data = fetch_data()
    for row in data:
        tree.insert("", tk.END, values=row)

root = tk.Tk()
root.title("База данных магазинов одежды")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tree = ttk.Treeview(frame, columns=("Name", "Price", "URL", "Image"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Price", text="Price")
tree.heading("URL", text="URL")
tree.heading("Image", text="Image")
tree.pack(fill=tk.BOTH, expand=True)

update_button = ttk.Button(root, text="Обновить данные", command=update_table)
update_button.pack(pady=10)
update_table()
root.mainloop()
