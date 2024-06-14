import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV and Excel files", "*.csv;*.xlsx")])
    return file_path

def list_columns(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please select a CSV or XLSX file.")
    return df.columns.tolist(), df

def sanitize_folder_name(name):
    return ''.join(c if c.isalnum() or c in (' ', '.', '-') else '.' for c in str(name))

def format_value(value):
    if isinstance(value, pd.Timestamp):
        return value.strftime("%d.%m.%Y")  # Formata como 'DD.MM.YYYY'
    return value

def create_folders(df, selected_columns):
    base_dir = os.path.join(os.getcwd(), "output_folders")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for _, row in df.iterrows():
        folder_name = " - ".join(sanitize_folder_name(format_value(row[col])) for col in selected_columns)
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    messagebox.showinfo("Success", f"Folders created in {base_dir}")

def main():
    file_path = select_file()
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return

    columns, df = list_columns(file_path)
    if not columns:
        messagebox.showerror("Error", "No columns found in the file")
        return

    root = tk.Tk()
    root.title("Select Columns")

    selected_columns = []

    def on_select():
        selected_columns[:] = [columns[i] for i in listbox.curselection()]
        root.quit()

    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    for col in columns:
        listbox.insert(tk.END, col)
    listbox.pack()

    select_button = tk.Button(root, text="Select", command=on_select)
    select_button.pack()

    root.mainloop()

    if selected_columns:
        create_folders(df, selected_columns)
    else:
        messagebox.showerror("Error", "No columns selected")

if __name__ == "__main__":
    main()
