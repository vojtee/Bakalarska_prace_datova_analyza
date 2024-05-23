import tkinter as tk
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


from tkinter import ttk, messagebox
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import utils

class AdvancedAnalytics:
    def __init__(self, master, notebook, tables, app):
        self.master = master
        self.app = app
        self.notebook = notebook
        self.tables = tables  # This should be a reference to the main data tables dictionary
        self.setup_styles()
        self.add_advanced_analytics_tab()

        # Hide the warning about future changes in pandas
        pd.set_option('future.no_silent_downcasting', True)

    def setup_styles(self):
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('TButton', font=('Helvetica', 10), padding=6, background='lightblue', foreground='black')
        style.map('TButton', background=[('active', 'mediumblue'), ('disabled', 'grey')])

        style.configure('TSaveButton', font=('Helvetica', 10), padding=6, background='lightgreen', foreground='white',
                        relief='raised', borderwidth=2)
        style.map('TSaveButton', background=[('active', 'green'), ('pressed', 'dark green'), ('disabled', 'grey')],
                   foreground=[('pressed', 'white'), ('active', 'white')])

        style.configure('TCloseButton', font=('Helvetica', 10), padding=6, background='lightcoral', foreground='white',
                        relief='raised', borderwidth=2)
        style.map('TCloseButton', background=[('active', 'red'), ('pressed', 'dark red'), ('disabled', 'grey')],
                   foreground=[('pressed', 'white'), ('active', 'white')])

    def add_advanced_analytics_tab(self):
        # Creating the tab for advanced analytics
        advanced_tab = ttk.Frame(self.notebook)
        self.notebook.add(advanced_tab, text="Pokročilá analýza")

        # Adding components to the advanced_tab
        ttk.Label(advanced_tab, text="Vyberte tabulky:", style='TLabel').pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
        self.table_listbox = tk.Listbox(advanced_tab, selectmode='extended', exportselection=False)
        self.table_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.table_listbox.bind('<<ListboxSelect>>', self.update_column_selection)

        ttk.Label(advanced_tab, text="Vyberte typ analýzy:", style='TLabel').pack(side=tk.TOP, fill=tk.X, padx=5,
                                                                                  pady=2)
        self.analysis_type_var = tk.StringVar()
        analysis_types = ["Lineární regrese", "Analýza korelací", "Spojení tabulek", "Agregace"]
        self.analysis_type_menu = ttk.Combobox(advanced_tab, textvariable=self.analysis_type_var, values=analysis_types,
                                               style='TCombobox')
        self.analysis_type_menu.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
        self.analysis_type_menu.bind('<<ComboboxSelected>>', self.update_analysis_options)

        self.init_analysis_options(advanced_tab)

        self.analysis_type_var.set("Lineární regrese")
        self.analysis_type_menu.event_generate('<<ComboboxSelected>>')

        ttk.Button(advanced_tab, text="Provést analýzu", command=self.execute_advanced_analysis, style='TButton').pack(
            side=tk.TOP, pady=5)

        # Fill the listbox with table names
        self.update_table_listbox()

    def init_analysis_options(self, parent):
        self.x_label = ttk.Label(parent, text="Vyberte sloupec X:", style='TLabel')
        self.x_column_var = tk.StringVar()
        self.x_column_menu = ttk.Combobox(parent, textvariable=self.x_column_var, style='TCombobox')

        self.y_label = ttk.Label(parent, text="Vyberte sloupec Y:", style='TLabel')
        self.y_column_var = tk.StringVar()
        self.y_column_menu = ttk.Combobox(parent, textvariable=self.y_column_var, style='TCombobox')

    def update_table_listbox(self):
        self.table_listbox.delete(0, tk.END)  # Odstranění stávajícího obsahu
        for table_name in self.tables.keys():  # Přidání aktualizovaného seznamu tabulek
            self.table_listbox.insert(tk.END, table_name)

    def update_analysis_options(self, event=None):
        analysis_type = self.analysis_type_var.get()
        if analysis_type == "Lineární regrese":
            self.x_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
            self.x_column_menu.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
            self.y_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
            self.y_column_menu.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
        else:
            self.x_label.pack_forget()
            self.x_column_menu.pack_forget()
            self.y_label.pack_forget()
            self.y_column_menu.pack_forget()

    def update_column_selection(self, event=None):
        selection = self.table_listbox.curselection()
        if not selection:
            return  # No selection made

        selected_table_name = self.table_listbox.get(selection[0])
        # Ensure that self.tables[selected_table_name] directly gives you the DataFrame
        df = self.tables[selected_table_name]

        # Extract column names from the DataFrame
        column_names = df.columns.tolist()

        # Update ComboBoxes for X and Y columns
        self.x_column_menu['values'] = column_names
        self.y_column_menu['values'] = column_names

        # Optionally clear the current selection in the ComboBoxes
        self.x_column_var.set('')
        self.y_column_var.set('')

    def reset_analysis_options(self):
        self.analysis_type_var.set("Lineární regrese")  # Reset analysis type to default
        self.analysis_type_menu.event_generate('<<ComboboxSelected>>')
        self.x_column_var.set('')  # Clear the selection for the X column
        self.y_column_var.set('')  # Clear the selection for the Y column
        self.x_column_menu['values'] = []  # Clear the dropdown values
        self.y_column_menu['values'] = []  # Clear the dropdown values

    def execute_advanced_analysis(self):
        selected_indices = self.table_listbox.curselection()
        if not selected_indices:
            messagebox.showinfo("Chyba", "Vyberte prosím alespoň jednu tabulku.")
            return

        selected_table_names = [self.table_listbox.get(i) for i in selected_indices]
        dfs = [self.tables[name] for name in selected_table_names]

        analysis_type = self.analysis_type_var.get()
        if analysis_type == "Lineární regrese":
            if len(dfs) != 1:
                messagebox.showerror("Chyba", "Lineární regrese vyžaduje právě jednu tabulku.")
                return
            self.perform_linear_regression(dfs[0])
        elif analysis_type == "Analýza korelací":
            if len(dfs) != 1:
                messagebox.showerror("Chyba", "Analýza korelací vyžaduje právě jednu tabulku.")
                return
            self.perform_correlation_analysis_and_plot(dfs[0])
        elif analysis_type == "Agregace":
            for df in dfs:
                self.perform_aggregation(df)
        elif analysis_type == "Spojení tabulek":
            if len(dfs) < 2:
                messagebox.showerror("Chyba", "Spojení tabulek vyžaduje alespoň dvě vybrané tabulky.")
                return
            self.join_tables_and_create_tab(dfs, selected_table_names)
        # Přidání dalších analýz podle potřeby

    def perform_linear_regression(self, df):
        x_column = self.x_column_var.get()
        y_column = self.y_column_var.get()

        if not x_column or not y_column:
            messagebox.showerror("Chyba", "Vyberte sloupce pro osy X a Y.")
            return

        # Check if selected columns are numeric and do not contain NaN values
        if df[x_column].dtype.kind not in 'fi' or df[x_column].isnull().any():
            messagebox.showerror("Chyba", "Vybraný sloupec X musí být číselný a nesmí obsahovat NaN hodnoty.")
            return
        if df[y_column].dtype.kind not in 'fi' or df[y_column].isnull().any():
            messagebox.showerror("Chyba", "Vybraný sloupec Y musí být číselný a nesmí obsahovat NaN hodnoty.")
            return

        X = df[[x_column]].values
        y = df[y_column].values

        # Create and predict using the model
        model = LinearRegression().fit(X, y)
        y_pred = model.predict(X)

        # Create the plot
        fig = Figure(figsize=(10, 8), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.scatter(X, y, color='blue')
        plot.plot(X, y_pred, color='red')
        plot.set_xlabel(x_column)
        plot.set_ylabel(y_column)
        plot.set_title('Lineární regrese')

        # Display the plot in a Tkinter window
        graph_window = tk.Toplevel(self.master)
        graph_window.title("Výsledek lineární regrese")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Optionally add a toolbar
        toolbar = NavigationToolbar2Tk(canvas, graph_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Button to save the plot
        save_button = ttk.Button(graph_window, text="Uložit graf", command=lambda: utils.save_graph(fig), style='TButton')
        save_button.pack(side=tk.BOTTOM)

    def perform_correlation_analysis_and_plot(self, df):
        numeric_df = df.select_dtypes(include=[np.number])

        # Kontrola, zda existují nějaké číselné sloupce pro analýzu
        if numeric_df.empty:
            messagebox.showerror("Chyba", "V datech nejsou žádné číselné sloupce k analýze.")
            return

        # Kontrola, zda existují NaN hodnoty ve sloupcích
        if numeric_df.isnull().any().any():
            messagebox.showerror("Chyba","Některé sloupce obsahují NaN hodnoty. Odstraňte nebo nahraďte tyto hodnoty a zkuste to znovu.")
            return

        # Calculate the correlation matrix
        corr_matrix = numeric_df.corr()

        # Plotting the heatmap
        fig, ax = plt.subplots(figsize=(10, 8))  # You can adjust the size as needed
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        ax.set_title('Matice korelací')

        # Display the plot in a new Tkinter window
        graph_window = tk.Toplevel(self.master)
        graph_window.title("Teplotní mapa korelací")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Optionally, add a toolbar
        toolbar = NavigationToolbar2Tk(canvas, graph_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Button to save the plot
        save_button = ttk.Button(graph_window, text="Uložit graf", command=lambda: utils.save_graph(fig), style='TButton')
        save_button.pack(side=tk.BOTTOM)

    def join_tables_and_create_tab(self, dfs, table_names):
        # Prefix columns with table name to differentiate them
        prefixed_dfs = []
        for df, name in zip(dfs, table_names):
            prefixed_columns = {col: f"{name}_{col}" for col in df.columns}
            prefixed_df = df.rename(columns=prefixed_columns)
            prefixed_dfs.append(prefixed_df)

        # Join the tables
        result_df = pd.concat(prefixed_dfs, axis=1)

        # Kontrola, zda spojené tabulky obsahují NaN hodnoty
        if result_df.isnull().any().any():
            messagebox.showerror("Chyba","Spojené tabulky obsahují NaN hodnoty. Odstraňte nebo nahraďte tyto hodnoty a zkuste to znovu.")
            return

        # Generate a descriptive name for the joined table
        joined_table_name = " & ".join(table_names) + " Joined"

        # Create a new tab for the joined table
        self.app.create_tab(result_df, joined_table_name)

    def perform_aggregation(self, df):
        numeric_df = df.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            if numeric_df.isnull().any().any():
                messagebox.showerror("Chyba",
                                     "Některé sloupce obsahují NaN hodnoty. Odstraňte nebo nahraďte tyto hodnoty a zkuste to znovu.")
                return

            aggregated_df = numeric_df.mean()

            # Create a top-level window
            result_window = tk.Toplevel(self.master)
            result_window.title("Agregované hodnoty")
            result_window.geometry("500x300")  # Adjusted size for better display

            # Frame to add some padding around the content
            frame = ttk.Frame(result_window, padding="10")
            frame.pack(fill=tk.BOTH, expand=True)

            # Text widget with a scrollbar
            text_scroll = tk.Scrollbar(frame)
            text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

            result_text = tk.Text(frame, wrap=tk.WORD, state='disabled', yscrollcommand=text_scroll.set,
                                  font=('Courier New', 10), borderwidth=2, relief="sunken")
            result_text.pack(fill=tk.BOTH, expand=True)

            # Enable the text widget, insert the data, then disable to prevent user editing
            result_text.config(state='normal')
            header = f"{'Column':<25}{'Value':>15}\n{'-' * 40}\n"
            result_text.insert(tk.END, header)
            for index, value in aggregated_df.items():  # Using .items() for compatibility
                formatted_line = f"{index:<25}{value:15.2f}\n"
                result_text.insert(tk.END, formatted_line)
            result_text.config(state='disabled')

            text_scroll.config(command=result_text.yview)

            # Close button at the bottom
            close_button = ttk.Button(frame, text="Zavřít", command=result_window.destroy, style='TButton')
            close_button.pack(side=tk.BOTTOM, pady=5)
        else:
            messagebox.showerror("Error", "Nejsou k dispozici žádná číselná data pro agregaci.")