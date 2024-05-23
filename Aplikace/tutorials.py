import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk

import tutorials_data



class TutorialManager:
    def __init__(self, master, notebook):
        self.master = master
        self.notebook = notebook
        self.setup_styles()
        self.add_tutorial_tab()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('TLabel', font=('Helvetica', 12), background='white', padding=10)
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=10, borderwidth=2, relief='flat')
        style.map('TButton', background=[('active', '#e1f5fe'), ('!active', 'lightgrey')],
                  foreground=[('active', '#009688'), ('!active', 'black')])
        style.configure('Heading.TLabel', font=('Helvetica', 16, 'bold'), background='white', foreground='#00574B')

    def add_tutorial_tab(self):
        self.tutorial_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tutorial_tab, text="Tutoriály")
        self.setup_tutorial_main_page()

    def setup_tutorial_main_page(self):
        for widget in self.tutorial_tab.winfo_children():
            widget.destroy()

        # Buttons for each tutorial category
        ttk.Button(self.tutorial_tab, text="Základní návody",
                   command=self.display_basic_tutorials).pack(fill='x', padx=20, pady=10)
        ttk.Button(self.tutorial_tab, text="Návody pro grafy",
                   command=self.display_graph_tutorials).pack(fill='x', padx=20, pady=10)
        ttk.Button(self.tutorial_tab, text="Pokročilé scénáře",
                   command=self.display_advanced_scenarios).pack(fill='x', padx=20, pady=10)

    def display_basic_tutorials(self):
        self.display_tutorials(tutorials_data.basic_tutorials, "Základní návody")

    def display_graph_tutorials(self):
        self.display_tutorials(tutorials_data.graph_tutorials, "Návody pro grafy")

    def display_advanced_scenarios(self):
        self.display_tutorials(tutorials_data.advanced_scenarios, "Pokročilé scénáře")

    def display_tutorials(self, tutorials, category_name):
        # Clear existing widgets in the tutorial tab
        for widget in self.tutorial_tab.winfo_children():
            widget.destroy()

        # Add a back button and a label for the category
        ttk.Button(self.tutorial_tab, text="Zpět", command=self.setup_tutorial_main_page).pack(side=tk.TOP, fill='x', padx=20, pady=5)
        ttk.Label(self.tutorial_tab, text=f"{category_name}", style='Heading.TLabel').pack(side=tk.TOP, fill='x', padx=20, pady=10)

        # Create buttons for each tutorial in the category
        for name, steps in tutorials.items():
            ttk.Button(self.tutorial_tab, text=name,
                       command=lambda s=steps, n=name: self.open_tutorial(s, n)).pack(fill='x', padx=20, pady=5)

    def open_tutorial(self, steps, name):
        tutorial_window = tk.Toplevel(self.master)
        tutorial_window.title(f"Tutoriál - {name}")
        tutorial_window.geometry("600x500")
        tutorial_window.minsize(600, 500)

        # Canvas and Scrollbar setup
        canvas = tk.Canvas(tutorial_window, highlightthickness=0)
        scrollbar = tk.Scrollbar(tutorial_window, orient="vertical", command=canvas.yview, width=12)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Layout using grid
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure the grid
        tutorial_window.grid_rowconfigure(0, weight=1)
        tutorial_window.grid_columnconfigure(0, weight=1)

        # Frame for content inside the canvas
        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor='nw')

        # Dynamic adjustment for the canvas scrollregion
        content_frame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        # Display tutorial steps and images
        step_title_label = ttk.Label(content_frame, text=f"{name}", font=('Helvetica', 14, 'bold'))
        step_title_label.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5)

        step_text = tk.StringVar(value="")
        step_label = ttk.Label(content_frame, textvariable=step_text, wraplength=560)
        step_label.pack(expand=True, side=tk.TOP, fill=tk.X, padx=20, pady=10)

        img_label = tk.Label(content_frame)
        img_label.pack(expand=True, side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

        # Adjust text and image dynamically
        def adjust_content():
            new_width = tutorial_window.winfo_width() - 40  # Assuming padding or margins total 40px
            step_label.config(wraplength=new_width)  # Adjust text wrapping
            if current_step[0] >= 0:  # If there is already a step shown, update image size too
                update_step(current_step[0])

        tutorial_window.bind('<Configure>', lambda e: adjust_content())  # Bind resizing of window

        # Buttons frame at the bottom
        buttons_frame = tk.Frame(tutorial_window)
        buttons_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

        # Previous and Next buttons
        prev_button = ttk.Button(buttons_frame, text="Zpět", command=lambda: update_step(current_step[0] - 1))
        next_button = ttk.Button(buttons_frame, text="Další", command=lambda: update_step(current_step[0] + 1))
        prev_button.pack(side='left', padx=10, pady=10)
        next_button.pack(side='right', padx=10, pady=10)

        # Manage steps
        current_step = [0]  # Tracking the current step

        def update_step(step_index):
            step_text.set(steps[step_index][0])
            img_path = steps[step_index][1]
            max_size = min(tutorial_window.winfo_width(),
                           tutorial_window.winfo_height()) - 100  # Adjust max size based on window
            if img_path and img_path != "no_image":
                img = self.resize_image_aspect_ratio(img_path, max_size)  # Resize with dynamic max dimension
                photo = ImageTk.PhotoImage(img)
                img_label.config(image=photo)
                img_label.image = photo
            else:
                img_label.config(image='')
            current_step[0] = step_index
            prev_button.config(state='normal' if current_step[0] > 0 else 'disabled')
            next_button.config(state='normal' if current_step[0] < len(steps) - 1 else 'disabled')

        update_step(0)  # Initialize with the first step

    def resize_image_aspect_ratio(self, img_path, max_size):
        img = Image.open(img_path)
        # Get the current size of the image
        original_width, original_height = img.size

        # Determine the scale factor, keeping the aspect ratio
        ratio = min(max_size / original_width, max_size / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

        # Resize the image using a resampling filter
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_img