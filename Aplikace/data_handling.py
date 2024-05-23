import pandas as pd
import os

from tkinter import filedialog, messagebox

# Function to open an Excel or CSV file and display its contents in a new tab
# Function to open an Excel or CSV file and display its contents in a new tab
def open_excel(app):
    if app.excel_file_count >= 5:
        messagebox.showerror("Chyba", "Lze otevřít maximálně 5 souborů.")
        return
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")])
    if file_path:
        if file_path in app.opened_files:
            messagebox.showerror("Chyba", "Tento soubor je již otevřen.")
            return

        # Determine file extension and load accordingly
        file_extension = os.path.splitext(file_path)[1]
        try:
            if file_extension in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path, header=0)
            elif file_extension == '.csv':
                df = pd.read_csv(file_path, header=0)
            else:
                messagebox.showerror("Chyba", "Nepodporovaný typ souboru.")
                return

            # Check if the file is empty or contains only one row
            if df.empty:
                messagebox.showerror("Chyba", "Soubor je prázdný.")
                return
            if len(df) == 1:
                messagebox.showerror("Chyba", "Soubor obsahuje pouze jeden řádek.")
                return

            # Check for missing data in any column
            if df.isnull().any().any():
                original_row_count = len(df)
                df.dropna(inplace=True)
                removed_rows_count = original_row_count - len(df)
                messagebox.showinfo("Čištění dat",
                                    f"Detekována chybějící data. {removed_rows_count} řádků bylo odstraněno.")

            app.excel_file_count += 1
            tab_name = os.path.basename(file_path)
            app.create_tab(df, tab_name, file_path)
            app.tables[tab_name] = df
            app.opened_files.add(file_path)

        except Exception as e:
            messagebox.showerror("Chyba při načítání souboru", f"Nastala chyba při načítání souboru: {str(e)}")