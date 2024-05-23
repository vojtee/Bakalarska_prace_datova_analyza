import tkinter as tk

from matplotlib.backend_bases import NavigationToolbar2
from pandastable import Table
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from tkinter import filedialog
from geopy import Nominatim, Point
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from shapely.geometry import Point
from functools import lru_cache



# tooltip class for providing a small pop-up window with information
class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def show_tip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# customtable for displaying pandas dataframes in a tkinter window
class CustomTable(Table):
    def __init__(self, parent=None, dataframe=None, **kwargs):
        super().__init__(parent, dataframe=dataframe, **kwargs)
        self.disable_all_interactions()

    def disable_all_interactions(self):
        """Disable all mouse and keyboard bindings to make the table non-interactive."""
        for seq in self.bind():
            self.unbind(seq)


# customtoolbar for displaying only the necessary buttons in the navigation toolbar
class CustomToolbar(NavigationToolbar2Tk):
    # Only display the toolbar buttons we need
    toolitems = [t for t in NavigationToolbar2.toolitems if t[0] in ('Home', 'Pan', 'Zoom', 'Forward', 'Back')]


def save_graph(fig):
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        fig.savefig(file_path)


@lru_cache(maxsize=500)  # Cache results to minimize API calls
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="DataScienceApp")
    try:
        location = geolocator.geocode(city_name)
        if location:
            return Point(location.longitude, location.latitude)
    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"Geocoding timeout or error for {city_name}: {e}")
    except Exception as e:
        print(f"General error geocoding {city_name}: {e}")
    return None


def async_geocode(data, city_column):
    coordinates = [get_coordinates(city) for city in data[city_column]]
    data['Longitude'] = [point.x if point else None for point in coordinates]
    data['Latitude'] = [point.y if point else None for point in coordinates]
    return data
