import re
import os
import getpass

from .integrations import Calculator, Calendar, Weather, Clock, Contacts, Files, Settings, Web

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

        # APP Integrations
        self.calculator = Calculator()
        self.calendar = Calendar()
        self.weather = Weather()
        self.clock = Clock()
        self.contacts = Contacts()
        self.files = Files()
        self.settings = Settings()
        self.web = Web()

        # Rows
        self.result_row = Adw.ActionRow()
        self.web_row = Adw.ActionRow()
        self.web_row.set_title(f"Search in web: ")
        self.web_row.set_subtitle(self.web.name)
        self.rows.append(self.result_row)
        self.rows.append(self.web_row)

        # Groups
        self.web_group = Adw.PreferencesGroup()
        self.web_group.set_title("Web")
        self.web_group.add(self.web_row)
        self.group.add(self.result_row)

        self.page.add(self.web_group)
        self.set_default_size(600, -1)
        # Connect to the "changed" signal of the GtkEntry
        self.search_entry.connect("changed", self.on_entry_changed)
        self.search_entry.set_size_request(600, 70)

    def on_entry_changed(self, search_entry):
        text = search_entry.get_text()  # Remove previous search results

        if text:
            self.set_size_request(600, 500)
            if re.match(self.calculator.pattern, text):
                result = self.calculator.calculate(text)
                if isinstance(result, int):
                    self.result_row.set_title(str(result))
                    self.result_row.set_subtitle(self.calculator.name)

            elif re.match(self.calendar.pattern, text):
                result = self.calendar.get_day_of_week(re.search(self.calendar.pattern, text))
                if isinstance(result, str):
                    self.result_row.set_title(result)
                    self.result_row.set_subtitle(self.calendar.name)

            #elif re.match(pattern[], text):

            #elif re.match(pattern[], text):

            #elif re.match(pattern[], text):
            else:
                self.group.hide()

            self.web_row.set_title(f"Search in web: {text}")
            self.web_row.set_subtitle(self.web.name)
        else:
            self.set_size_request(600, -1)
            self.result_row.set_title("")
            self.result_row.set_subtitle("")
            self.web_row.set_title(f"Search in web: ")


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
