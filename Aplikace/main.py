import tkinter as tk

from data_science_app import DataScienceApp


def main():
    root = tk.Tk()
    app = DataScienceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
