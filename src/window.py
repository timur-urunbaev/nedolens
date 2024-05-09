import re
import os

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/nedogeek/nedolens/window.ui')
class NedolensWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NedolensWindow'

    search_entry = Gtk.Template.Child()
    page = Gtk.Template.Child()
    group = Gtk.Template.Child()

    def __init__(self, **kwargs):
      
        super().__init__(**kwargs)
        self.rows = []
        self.set_default_size(600, -1)

        # Connect to the "changed" signal of the GtkEntry
        self.search_entry.connect("changed", self.on_entry_changed)
        self.search_entry.set_size_request(600, 70)

    def on_entry_changed(self, search_entry):
        text = search_entry.get_text()  # Remove previous search results
        pattern = {
            'calculator': r'^[\d\s\(\)\+\-\*\/\^\%\.,]|sin|cos|tan|asin|acos|atan|exp|sqrt|log|log10|factorial|pi$',
            'calendar': '',
            'weather': '',
            'clock': '',
            'contacts': '',
            'web': '',
            'files': ,
            'settings': ,
        }

        if text:
            self.set_size_request(600, 500)
            if re.match()
            self.add_row(text, "temp")
            # self.search_and_display(text)
        else:
            self.set_size_request(600, -1)
            self.remove_all_rows(self.group)


    def add_group(self):
        # Add action row dynamically
        group = Adw.PreferencesGroup()
        self.page.add(group, False, False, 0)
        group.show_all()

    def remove_all_rows(self, group):
        for child in self.rows:
            group.remove(child)

    def add_row(self, result, integration="?"):
        # Add action row dynamically
        action_row = Adw.ActionRow()
        self.rows.append(action_row)
        self.group.add(action_row)
        action_row.set_title(result)
        action_row.set_subtitle(integration)
