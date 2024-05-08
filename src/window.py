import re
import os

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(filename='src//window.ui')
class NedolensWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NedolensWindow'

    box = Gtk.Template.Child()
    search_entry = Gtk.Template.Child()
    page = Gtk.Template.Child()
    group = Gtk.Template.Child()

    def __init__(self, **kwargs):
      
        super().__init__(**kwargs)
        self.set_default_size(600, -1)

        # Connect to the "changed" signal of the GtkEntry
        self.search_entry.connect("changed", self.on_entry_changed)
        self.search_entry.set_size_request(600, 70)

    def on_entry_changed(self, search_entry):
        text = search_entry.get_text()  # Remove previous search results

        if text:
          
            self.set_size_request(600, 500)
            self.search_and_display(text)
        else:
            self.set_size_request(600, -1)
            self.remove_all_rows(self.group)


    def search_and_display(self, query):
        base_path = 'C:/Users/admin/programming/python/nedolens'  # Set your base directory path
        for root, dirs, files in os.walk(base_path):
            for name in dirs + files:
                if query.lower() in name.lower():
                    self.add_row(os.path.join(root, name), "File" if os.path.isfile(os.path.join(root, name)) else "Directory")


    def add_group(self):
        # Add action row dynamically
        group = Adw.PreferencesGroup()
        self.page.add(group, False, False, 0)
        group.show_all()

    def remove_all_rows(group):
        children = group.get_children()
        for child in children:
            group.remove(child)

    def add_row(self, result, integration="?"):
        # Add action row dynamically
        action_row = Adw.ActionRow()
        self.group.add(action_row)
        action_row.set_title(result)
        action_row.set_subtitle(integration)
