import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import utils
import data_handling
import tutorials
import graphing
import advanced_analytics


class DataScienceApp:
    def __init__(self, master):
        self.master = master
        self.excel_file_count = 0  # Tracks actual Excel files opened
        self.joined_table_count = 0  # Tracks joined tables or dynamic tabs
        self.opened_files = set()  # Set to track opened files

        style = ttk.Style()
        # style.theme_use('clam')
        # Configure styles for the different widget types
        style.configure('TFrame',
                        background='white')

        style.configure('TButton',
                        font=('Helvetica', 10),
                        padding=6,
                        background='lightblue',
                        foreground='black')
        style.map('TButton',
                  background=[('active', 'mediumblue'), ('disabled', 'grey')])

        style.configure('TLabel',
                        font=('Helvetica', 12, 'bold'),
                        background='white',
                        foreground='black')

        style.configure('TNotebook',
                        background='white',
                        borderwidth=0)
        style.configure('TNotebook.Tab',
                        font=('Helvetica', 10, 'bold'),
                        padding=[10, 5],
                        background='lightgrey')
        style.map('TNotebook.Tab',
                  background=[('selected', 'lightgray'), ('!selected', 'white')])

        # Create a menu bar
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        self.master.title("DataStart")
        self.master.geometry('800x600')  # Set initial size of the window

        # Create a file menu
        self.file_menu = tk.Menu(menu, tearoff=0)  # Changed to an instance variable for access in other methods
        menu.add_cascade(label="Soubor", menu=self.file_menu)
        self.file_menu.add_command(label="Otevřít soubor...", command=lambda: data_handling.open_excel(self))

        # Create a Notebook widget
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        # Initialize the tables dictionary
        self.tables = {}

        # Create a welcome tab
        self.add_welcome_tab()

        # Create a tutorial tab
        self.tutorial_manager = tutorials.TutorialManager(master, self.notebook)

        # Create a graphing tab
        self.graphing_manager = graphing.GraphingTools(master, self)

        # Create an advanced analytics tab
        self.advanced_analytics = advanced_analytics.AdvancedAnalytics(master, self.notebook, self.tables, self)

    def create_tab(self, data, tab_name, file_path=None):
        # Create a new tab
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_name)

        # Add basic data analytics capabilities
        self.graphing_manager.add_analytics_widgets(tab, data, tab_name, file_path)

        # Add table widget to display sheet data
        table_frame = ttk.Frame(tab)
        table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        table_widget = utils.CustomTable(table_frame, dataframe=data, showtoolbar=False, showstatusbar=False)
        table_widget.show()

        # Store the DataFrame, not the Table widget, in the tables dictionary
        self.tables[tab_name] = data

        # Updates the table listbox in the advanced analytics tab
        self.advanced_analytics.update_table_listbox()

        # Only add the file to the opened_files set if a file_path is provided
        if file_path:
            self.opened_files.add(file_path)

    def close_tab(self, tab, tab_name, file_path):
        # Ask user if they are sure about closing the tab
        if messagebox.askyesno("Potvrzení zavření", f"Opravdu chcete zavřít záložku '{tab_name}'?"):
            # Remove the tab from the notebook
            self.notebook.forget(tab)

            # Update internal structures
            if tab_name in self.tables:
                del self.tables[tab_name]  # Remove from tables dictionary
            if file_path and file_path in self.opened_files:
                self.opened_files.remove(file_path)  # Remove from opened files set

            # Decrease the count of open files
            self.excel_file_count -= 1

            # Update the listbox
            self.advanced_analytics.update_table_listbox()
            self.advanced_analytics.reset_analysis_options()

    def add_welcome_tab(self):
        welcome_tab = ttk.Frame(self.notebook)
        self.notebook.add(welcome_tab, text="Vítejte")

        # Create a Canvas to allow for more flexible layout options
        canvas = tk.Canvas(welcome_tab)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Frame within the Canvas to hold the text
        text_frame = ttk.Frame(canvas)
        # Modify the anchor to 'nw' and adjust the x and y positioning to ensure uniform text alignment
        canvas.create_window((0, 0), window=text_frame, anchor="nw")

        # Define the welcome message with better formatting
        welcome_message = """
Vítejte v aplikaci DataStart!

Tato aplikace byla vytvořena Vojtěchem Hořejším jako součást jeho bakalářské práce. Cílem aplikace je poskytnout uživatelům nástroje pro základní analýzu dat a zároveň je seznámit se základy datové vědy.

Hlavní funkce aplikace:
- Nahrávání dat: Umožňuje uživatelům nahrávat data přímo z Excelových a CSV souborů.
- Analýza dat: Nabízí nástroje pro základní statistické analýzy a vizualizace dat.
- Edukativní obsah: Tutoriály a návody provádějí uživatele krok za krokem.

Jak začít:
Pro začátek otevřete soubor prostřednictvím menu 'Soubor'. Ujistěte se, že první řádek vašeho souboru obsahuje názvy sloupců a pod nimi jsou data. Maximálně můžete mít nahráno pět souborů současně.

Pro orientaci a další informace o používání aplikace navštivte záložku 'Tutoriály', kde naleznete podrobné návody a postupy. V tutoriálech najdete základní návody a grafy, které vám pomohou seznámit se s aplikací. Dále jsou zde pokročilé scénáře, které vás provedou analýzou vybraných hypotéz. Na konci každého scénáře naleznete několik otázek, na které se můžete pokusit odpovědět a vyhledat potřebné informace.

Upozornění:
Pokud používáte geografické grafy, aplikace se může na chvíli zaseknout během načítání dat. Prosím, nevypínejte ji.

Tato aplikace slouží nejen k praktickému zvládnutí základů datové vědy, ale také jako pedagogický nástroj pro vzdělávání v oblasti analýzy dat.
"""

        # Display the welcome message
        welcome_label = tk.Label(text_frame, text=welcome_message, justify="left", anchor="nw",
                                 wraplength=canvas.winfo_reqwidth() - 20,  # Adjust wraplength dynamically
                                 padx=20, pady=20, font=("Helvetica", 11))
        welcome_label.pack(fill=tk.BOTH, expand=True)

        # Ensure the text frame adjusts to the canvas size changes
        text_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Ensure the wrap length adjusts to the window width dynamically
        canvas.bind("<Configure>", lambda e: welcome_label.config(wraplength=canvas.winfo_width() - 40))
