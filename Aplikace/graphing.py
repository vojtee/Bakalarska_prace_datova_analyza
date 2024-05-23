import tkinter as tk
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import folium
import os


from tkinter import ttk, messagebox


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from tkinterweb.htmlwidgets import HtmlFrame

import utils


class GraphingTools:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.setup_styles()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=10)
        style.configure('TLabel', font=('Helvetica', 12), background='white')
        style.configure('Heading.TLabel', font=('Helvetica', 14, 'bold'), background='white', foreground='#333')
        style.configure('TNotebook', background='white', borderwidth=1)
        style.configure('TNotebook.Tab', font=('Helvetica', 10, 'bold'), padding=(5, 5), background='lightgrey')

    def update_graph_options(self, graph_type_var, graph_type_label, graph_type_menu, x_label, x_column_menu, y_label,
                             y_columns_listbox, generate_button, help_button):
        graph_type = graph_type_var.get()

        # Hide all components initially
        graph_type_label.grid_remove()
        graph_type_menu.grid_remove()
        x_label.grid_remove()
        x_column_menu.grid_remove()
        y_label.grid_remove()
        y_columns_listbox.grid_remove()
        generate_button.grid_remove()
        help_button.grid_remove()

        # Common placement for graph type selection
        graph_type_label.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=(10, 0))
        graph_type_menu.grid(row=1, column=0, columnspan=2, sticky='ew', padx=10, pady=(0, 10))

        if graph_type == "Kruhový graf":
            # Settings for Pie Chart
            x_label.config(text="Vyberte sloupec štítků:")
            y_label.config(text="Vyberte sloupce dat:")
            y_columns_listbox.config(selectmode='extended')
            x_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
            x_column_menu.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
            y_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=10)
            y_columns_listbox.grid(row=5, column=0, columnspan=2, sticky='ew', padx=10)
        elif graph_type == "Geografický graf":
            # Settings for Geographic Chart
            x_label.config(text="Vyberte sloupec s názvem města:")
            y_label.config(text="Vyberte sloupec pro velikost bublin:")
            y_columns_listbox.config(selectmode='browse')
            x_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
            x_column_menu.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
            y_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=10)
            y_columns_listbox.grid(row=5, column=0, columnspan=2, sticky='ew', padx=10)
        elif graph_type in ["Histogram", "Krabicový graf"]:
            # Settings for Histogram and Box Plot
            y_label.config(text="Vyberte sloupce dat:")
            y_columns_listbox.config(selectmode='extended')
            y_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
            y_columns_listbox.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
        else:
            # Settings for other graph types (Line, Bar, Scatter)
            x_label.config(text="Vyberte sloupec osy X:")
            y_label.config(text="Vyberte sloupce osy Y (použijte Ctrl pro více):")
            y_columns_listbox.config(selectmode='extended')
            x_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
            x_column_menu.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
            y_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=10)
            y_columns_listbox.grid(row=5, column=0, columnspan=2, sticky='ew', padx=10)

        generate_button.grid(row=6, column=0, pady=10, padx=10)
        help_button.grid(row=6, column=1, pady=10, padx=10)

    def calculate_max_width(self, columns, max_width=100):
        max_column_length = max(len(column) for column in columns)
        return min(max_column_length, max_width)

    def add_analytics_widgets(self, tab, data, tab_name, file_path):
        # Create buttons to display analytics and close button
        # Create a frame for the buttons
        button_frame = tk.Frame(tab)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        # Button to close the tab, aligned to the top-right corner
        close_button = ttk.Button(button_frame, text="X", command=lambda: self.app.close_tab(tab, tab_name, file_path))
        close_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Frame for "Show Statistics"
        stats_frame = tk.Frame(button_frame)
        stats_frame.pack(side=tk.LEFT, padx=10)
        show_stats_button = ttk.Button(stats_frame, text="Zobrazit statistiky", command=lambda: self.show_stats(data))
        show_stats_button.pack(side=tk.LEFT)
        stats_help_text = "Zobrazí základní statistiky, jako jsou průměr, medián atd."
        self.create_tooltip(show_stats_button, "Zobrazit základní statistiky pro každý sloupec.")
        self.create_help_icon(stats_frame, stats_help_text)

        # Frame for "Show Graph"
        graph_frame = tk.Frame(button_frame)
        graph_frame.pack(side=tk.LEFT, padx=10)
        show_graph_button = ttk.Button(graph_frame, text="Zobrazit graf", command=lambda: self.show_graph(data))
        show_graph_button.pack(side=tk.LEFT)
        graph_help_text = "Generuje různé typy grafů pro vizualizaci dat."
        self.create_tooltip(show_graph_button, "Generovat grafy, jako jsou sloupcové, spojnicové atd.")
        self.create_help_icon(graph_frame, graph_help_text)

    def create_help_icon(self, parent, help_text):
        # Create the help icon button and position it next to other elements
        help_button = tk.Button(parent, text="?", bg="light gray",
                                command=lambda: messagebox.showinfo("Nápověda", help_text))
        help_button.pack(side=tk.LEFT, padx=(5, 0))
        return help_button

    def create_tooltip(self, widget, text):
        tool_tip = utils.ToolTip(widget)
        widget.bind('<Enter>', lambda event: tool_tip.show_tip(text))
        widget.bind('<Leave>', lambda event: tool_tip.hide_tip())

    def show_graph_help(self):
        # Paths to images for each graph type - these need to be set to the correct file paths
        graph_images = {
            "Spojnicový graf": "resources/graph_helper_pictures/line_graph_example.png",
            "Sloupcový graf": "resources/graph_helper_pictures/bar_graph_example.png",
            "Bodový graf": "resources/graph_helper_pictures/scatter_plot_example.png",
            "Kruhový diagram": "resources/graph_helper_pictures/pie_chart_example.png",
            "Histogram": "resources/graph_helper_pictures/histogram_example.png",
            "Krabicový graf": "resources/graph_helper_pictures/box_plot_example.png",
            "Geografický graf": "resources/graph_helper_pictures/geographic_map_example.png"
        }

        # Text descriptions for each graph type
        # Text descriptions for each graph type
        help_texts = {
            "Spojnicový graf": (
                "Spojnicové grafy jsou ideální pro zobrazení trendů v čase. "
                "Jsou vhodné pro spojité údaje a zobrazují, jak se data mění "
                "v průběhu času. Například je můžete použít pro sledování změn "
                "teplot, cen akcií nebo počtu obyvatel v průběhu let."
            ),
            "Sloupcový graf": (
                "Sloupcové grafy jsou skvělé pro porovnání množství mezi různými "
                "skupinami nebo kategoriemi. Pomocí nich můžete vizualizovat rozdíly "
                "v datech, jako jsou srovnání prodejů různých produktů, počtu studentů "
                "v různých třídách nebo množství srážek v různých městech."
            ),
            "Bodový graf": (
                "Bodové grafy slouží k identifikaci vztahů mezi dvěma proměnnými. "
                "Pomáhají zjistit, zda existuje korelace mezi dvěma sadami dat. "
                "Například můžete použít bodový graf k analýze vztahu mezi věkem a příjmem "
                "nebo mezi počtem hodin strávených studiem a výsledky zkoušek."
            ),
            "Kruhový diagram": (
                "Kruhové diagramy jsou nejvhodnější pro zobrazení části celku. "
                "Jsou ideální, pokud chcete ukázat procentuální rozložení jednotlivých "
                "kategorií. Například můžete vizualizovat podíl jednotlivých výdajových položek "
                "v rozpočtu, rozdělení hlasů v anketě nebo procentuální zastoupení různých "
                "druhů ovoce v celkové produkci."
            ),
            "Histogram": (
                "Histogramy slouží k zobrazení rozdělení proměnných a identifikaci vzorců, "
                "jako je šikmost nebo bimodalita. Jsou užitečné pro analýzu frekvence "
                "výskytu hodnot v datech. Například můžete zobrazit, kolikrát se určitá "
                "hodnota vyskytuje v souboru dat, jako jsou výsledky testů, věkové skupiny "
                "nebo výšky lidí."
            ),
            "Krabicový graf": (
                "Krabicové grafy dobře ukazují, jak jsou hodnoty v datech rozloženy, a jsou "
                "zvláště užitečné pro detekci odlehlých hodnot. Pomocí nich můžete rychle "
                "získat přehled o mediánu, kvantilech a rozptylech dat. Například je můžete "
                "použít k analýze výšky studentů ve třídě nebo k hodnocení rozložení platů "
                "v rámci firmy."
            ),
            "Geografický graf": (
                "Geografické grafy zobrazují data na mapě a jsou užitečné pro vizualizaci "
                "geografických dat. Pomáhají identifikovat geografické trendy a vzory. "
                "Například můžete zobrazit distribuci populace, hustotu výskytu určitých druhů "
                "rostlin nebo rozložení zákazníků podle regionu."
            )
        }

        # Create a new window or dialog to display this information
        info_window = tk.Toplevel(self.master)
        info_window.title("Informace o grafech")

        # Create a notebook widget
        notebook = ttk.Notebook(info_window)
        notebook.pack(expand=1, fill="both")

        # Create tabs for each graph type
        for graph_type, desc in help_texts.items():
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=graph_type)

            # Set up the layout in each tab
            frame = ttk.Frame(tab)
            frame.pack(fill="both", expand=True)

            # Load and display the image
            image_path = graph_images[graph_type]
            img = Image.open(image_path)
            img = img.resize((400, 400))  # Resize image
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=photo)
            img_label.image = photo  # keep a reference
            img_label.pack(side="left", padx=10, pady=10)

            # Display the description
            text = tk.Text(frame, wrap="word", height=10, width=50, font=('Helvetica', 14))  # Increase font size
            text.insert("end", desc)
            text.config(state="disabled")
            text.pack(side="left", fill="both", expand=True)

        info_window.mainloop()

    def show_stats(self, data):
        stats_window = tk.Toplevel(self.master)
        stats_window.title("Základní statistiky")
        stats_window.geometry("600x400")  # Adjust size as needed

        # Generate basic statistics and reset index to get column names as a regular column
        basic_stats = data.describe().transpose().reset_index()
        basic_stats.rename(columns={'index': 'Název sloupce'}, inplace=True)

        # Mapping English terms to Czech
        translations = {
            'count': 'Počet',
            'mean': 'Průměr',
            'std': 'Směrodatná odchylka',
            'min': 'Min',
            '25%': '25. percentil',
            '50%': 'Medián',
            '75%': '75. percentil',
            'max': 'Max'
        }
        basic_stats.rename(columns=translations, inplace=True)

        # Creating a frame for the Treeview and scrollbars
        stats_frame = tk.Frame(stats_window)
        stats_frame.pack(fill="both", expand=True)

        # Defining the columns based on the DataFrame's statistics columns
        columns = list(basic_stats.columns)
        stats_tree = ttk.Treeview(stats_frame, columns=columns, show="headings", height=400)

        # Configuring each column in the Treeview
        for col in columns:
            stats_tree.heading(col, text=col)
            stats_tree.column(col, anchor="center", width=100)

        # Inserting rows into the Treeview
        for _, row in basic_stats.iterrows():
            stats_tree.insert("", tk.END, values=row.tolist())

        # Adding scrollbars
        vsb = ttk.Scrollbar(stats_frame, orient="vertical", command=stats_tree.yview)
        hsb = ttk.Scrollbar(stats_frame, orient="horizontal", command=stats_tree.xview)
        stats_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        stats_tree.pack(side="top", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")

    def show_graph(self, data):
        graph_window = tk.Toplevel(self.master)
        graph_window.title("Vytvořit graf")
        frame = tk.Frame(graph_window)
        frame.pack(padx=10, pady=10)

        graph_type_label = tk.Label(frame, text="Vyberte typ grafu:", justify='center')
        graph_type_label.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=(10, 0))

        graph_types = ["Spojnicový graf", "Sloupcový graf", "Bodový graf", "Kruhový graf", "Histogram",
                       "Krabicový graf", "Geografický graf"]
        graph_type_var = tk.StringVar(value=graph_types[0])

        graph_type_menu = ttk.Combobox(frame, textvariable=graph_type_var, values=graph_types, width=25,
                                       state="readonly")
        graph_type_menu.grid(row=1, column=0, columnspan=2, sticky='ew', padx=10, pady=(0, 10))
        graph_type_menu.bind("<<ComboboxSelected>>",
                             lambda _: self.update_graph_options(graph_type_var, graph_type_label, graph_type_menu,
                                                                 x_label,
                                                                 x_column_menu, y_label,
                                                                 y_columns_listbox, generate_button, help_button))

        x_label = tk.Label(frame, text="Vyberte sloupec osy X:", justify='center')
        x_column_var = tk.StringVar()
        x_column_menu = ttk.Combobox(frame, textvariable=x_column_var, values=list(data.columns),
                                     width=self.calculate_max_width(data.columns))

        y_label = tk.Label(frame, text="Vyberte sloupce osy Y:", justify='center')
        y_columns_listbox = tk.Listbox(frame, selectmode='extended', exportselection=False,
                                       width=self.calculate_max_width(data.columns))
        for column in data.columns:
            y_columns_listbox.insert('end', column)

        help_button = ttk.Button(frame, text="?", command=self.show_graph_help)
        generate_button = ttk.Button(frame, text="Generovat graf",
                                     command=lambda: self.generate_graph(data, graph_type_var.get(), x_column_var.get(),
                                                                         [y_columns_listbox.get(i) for i in
                                                                          y_columns_listbox.curselection()]))

        self.update_graph_options(graph_type_var, graph_type_label, graph_type_menu, x_label, x_column_menu, y_label,
                                  y_columns_listbox, generate_button, help_button)

    def generate_graph(self, data, graph_type, x_column, y_columns):
        if not x_column:
            messagebox.showerror("Chyba", "Vyberte sloupec pro osu X.")
            return

        if not y_columns:
            messagebox.showerror("Chyba", "Vyberte alespoň jeden sloupec pro osu Y.")
            return

        if graph_type == "Geografický graf" and len(y_columns) != 1:
            messagebox.showerror("Chyba", "Pro geografický graf vyberte pouze jeden sloupec pro osu Y.")
            return

        fig, ax = plt.subplots(figsize=(8, 6))
        try:
            if graph_type == "Spojnicový graf":
                self.plot_line_graph(data, x_column, y_columns, ax)
            elif graph_type == "Sloupcový graf":
                self.plot_bar_graph(data, x_column, y_columns, ax)
            elif graph_type == "Bodový graf":
                self.plot_scatter_graph(data, x_column, y_columns, ax)
            elif graph_type == "Kruhový graf":
                self.plot_pie_chart(data, x_column, y_columns, ax)
            elif graph_type == "Histogram":
                self.plot_histogram(data, y_columns, ax)
            elif graph_type == "Krabicový graf":
                self.plot_box_plot(data, y_columns, ax)
            elif graph_type == "Geografický graf":
                self.plot_geographic_map(data, x_column, y_columns[0])
            else:
                messagebox.showerror("Chyba", "Neznámý typ grafu.")
                return
        except Exception as e:
            messagebox.showerror("Chyba", f"Nastala chyba při generování grafu: {str(e)}")
            return

        if graph_type != "Geografický graf":
            self.display_graph(fig, ax)

    def plot_line_graph(self, data, x_column, y_columns, ax):
        for y_column in y_columns:
            if not pd.api.types.is_numeric_dtype(data[y_column]):
                raise ValueError(
                    f"Sloupec '{y_column}' neobsahuje číselné hodnoty a nelze jej použít pro spojnicový graf.")
            ax.plot(data[x_column], data[y_column], label=y_column)
        ax.set_xlabel(x_column)
        ax.set_ylabel("Hodnota")
        ax.set_title("Spojnicový graf")
        ax.legend()

    def plot_bar_graph(self, data, x_column, y_columns, ax):
        width = 0.2  # Width of each bar

        # Check if all y_columns contain numeric data
        for y_column in y_columns:
            if not pd.api.types.is_numeric_dtype(data[y_column]):
                raise ValueError(
                    f"Sloupec '{y_column}' neobsahuje číselné hodnoty a nemůže být agregován pro sloupcový graf.")

        # Aggregate data by summing up y values for each x value
        aggregated_data = data.groupby(x_column)[y_columns].sum().reset_index()
        x_unique = aggregated_data[x_column]  # Unique values for x axis
        positions = range(len(x_unique))  # Positions for x axis

        # Plot each y_column
        for i, y_column in enumerate(y_columns):
            y_values = aggregated_data[y_column].values  # Get aggregated values for the y column
            if len(y_values) != len(x_unique):
                raise ValueError(f"Neodpovídající délky mezi sloupci osy X a Y: {x_column} a {y_column}")

            ax.bar([p + width * i for p in positions], y_values, width, label=y_column)

        ax.set_xticks([p + width * (len(y_columns) - 1) / 2 for p in positions])
        ax.set_xticklabels(x_unique)
        ax.set_xlabel(x_column)
        ax.set_ylabel("Hodnota")
        ax.set_title("Sloupcový graf")
        ax.legend()
        plt.tight_layout()  # Automatic alignment of plot elements

    def plot_scatter_graph(self, data, x_column, y_columns, ax):
        for y_column in y_columns:
            if not pd.api.types.is_numeric_dtype(data[y_column]):
                raise ValueError(f"Sloupec '{y_column}' neobsahuje číselné hodnoty a nelze jej použít pro bodový graf.")
            ax.scatter(data[x_column], data[y_column], label=y_column)
        ax.set_xlabel(x_column)
        ax.set_ylabel("Hodnota")
        ax.set_title("Bodový graf")
        ax.legend()

    def plot_pie_chart(self, data, x_column, y_columns, ax):
        if len(data) > 1:
            # Aggregate data by x_column and sum the y_columns
            aggregated_data = data.groupby(x_column)[y_columns].sum().reset_index()
            # Combine y_columns into one column for pie chart
            aggregated_data['sum'] = aggregated_data[y_columns].sum(axis=1)
            ax.pie(aggregated_data['sum'], labels=aggregated_data[x_column], autopct='%1.1f%%', startangle=90)
        else:
            single_row = data.iloc[0][y_columns]
            if not all(pd.api.types.is_numeric_dtype(single_row[col]) for col in y_columns):
                raise ValueError("Všechny vybrané sloupce pro kruhový graf musí obsahovat číselné hodnoty.")
            ax.pie(single_row, labels=single_row.index, autopct='%1.1f%%', startangle=90)
        ax.set_title("Kruhový graf")

    def plot_histogram(self, data, y_columns, ax):
        for y_column in y_columns:
            if not pd.api.types.is_numeric_dtype(data[y_column]):
                raise ValueError(f"Sloupec '{y_column}' neobsahuje číselné hodnoty a nelze jej použít pro histogram.")
            values = data[y_column].dropna()
            bins = int(len(values) ** 0.5)
            ax.hist(values, bins=bins, label=y_column, alpha=0.7, edgecolor='black')

        ax.set_xlabel("Hodnota")
        ax.set_ylabel("Četnost")
        ax.set_title("Histogram")
        ax.legend()
        ax.grid(True)

    def plot_box_plot(self, data, y_columns, ax):
        values = []
        for y_column in y_columns:
            if not pd.api.types.is_numeric_dtype(data[y_column]):
                raise ValueError(
                    f"Sloupec '{y_column}' neobsahuje číselné hodnoty a nelze jej použít pro krabicový graf.")
            values.append(data[y_column].dropna())

        ax.boxplot(values, patch_artist=True, notch=True, vert=True, showmeans=True)
        ax.set_xticklabels(y_columns, rotation=45, ha='right')
        ax.set_xlabel("Sloupce")
        ax.set_ylabel("Hodnota")
        ax.set_title("Krabicový graf")
        ax.grid(True)

    def plot_geographic_map(self, data, x_column, y_column):
        try:
            data = utils.async_geocode(data, x_column)
        except Exception as e:
            messagebox.showerror("Chyba", f"Nastala chyba při geokódování: {str(e)}")
            return

        if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
            messagebox.showerror("Chyba", "Geokódování selhalo nebo chybí souřadnice.")
            return

        plot_data = data.dropna(subset=['Latitude', 'Longitude', y_column])
        filepath = os.path.abspath('map.html')

        m = folium.Map(location=[plot_data['Latitude'].mean(), plot_data['Longitude'].mean()], zoom_start=10,
                       tiles='OpenStreetMap')

        for idx, row in plot_data.iterrows():
            if row[y_column] > 0:
                folium.CircleMarker(
                    location=[row['Latitude'], row['Longitude']],
                    radius=float(row[y_column]) / 1000,
                    popup=f"{row[x_column]}: {row[y_column]}",
                    tooltip=row[x_column],
                    color='blue',
                    fill=True
                ).add_to(m)

        m.save(filepath)
        self.open_map_in_browser(filepath)

    def open_map_in_browser(self, filepath):
        # Check if the path is a string and open it in the default web browser
        if isinstance(filepath, str):
            webbrowser.open_new_tab(filepath)
        else:
            print("Invalid filepath. It must be a string.")

    # Depricated method of plotting graphs inside the app
    def display_html_in_tkinter(self, html_path):
        # Create a new top-level window
        map_window = tk.Toplevel(self.master)
        map_window.title("Map View")
        map_window.geometry("800x600")  # Adjust size as necessary

        # Check if the file exists and print an error message if not
        if not os.path.exists(html_path):
            tk.messagebox.showerror("Error", "HTML file not found.")
            return

        # Create a Frame for the browser widget
        frame = tk.Frame(map_window)
        frame.grid(row=0, column=0, sticky="nsew")  # Grid method used here

        map_window.grid_rowconfigure(0, weight=1)
        map_window.grid_columnconfigure(0, weight=1)

        # Embed the HTML map in the frame using tkinterweb
        browser = HtmlFrame(frame, horizontal_scrollbar="auto")
        browser.load_file(html_path)
        browser.grid(row=0, column=0, sticky="nsew")  # Grid method used here

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Add a download button
        download_button = tk.Button(map_window, text="Download Map", command=lambda: self.download_map(html_path))
        download_button.grid(row=1, column=0, pady=10)

    def display_graph(self, fig, ax):
        graph_window = tk.Toplevel(self.master)
        graph_window.title("Graf")

        # Tvorba plátna pro graf
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = utils.CustomToolbar(canvas, graph_window)
        toolbar.update()
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Funkce pro přepnutí mřížky
        def toggle_grid():
            ax.grid()  # Toggle the grid
            canvas.draw_idle()  # Redraw the figure

        # Tlačítko pro přepnutí mřížky
        toggle_button = tk.Button(graph_window, text="Přepnout mřížku", command=toggle_grid)
        toggle_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Tlačítko pro uložení grafu
        save_button = tk.Button(graph_window, text="Uložit graf", command=lambda: utils.save_graph(fig))
        save_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def update_canvas(self, ax):
        fig = ax.get_figure()
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)