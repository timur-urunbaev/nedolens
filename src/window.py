import re
import os

from .integrations import Calculator, Calendar, Weather, Clock, Contacts, Files, Settings, Web

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio

@Gtk.Template(resource_path='/com/nedogeek/nedolens/window.ui')
class NedolensWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NedolensWindow'

    search_entry = Gtk.Template.Child()
    page = Gtk.Template.Child()

    def __init__(self, **kwargs):
      
        super().__init__(**kwargs)

        # Signals
        self.search_entry.connect("changed", self.on_entry_changed)
        #self.connect("key-press-event", self.on_key_press)

        # Dimensions and Window Size
        self.search_entry.set_size_request(600, 70)
        self.set_default_size(600, -1)

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

        # Icons
        self.web_icon = Gtk.Image.new_from_icon_name(self.web.icon)
        self.calculator_icon = Gtk.Image.new_from_icon_name(self.calculator.icon)

        # Result Row
        self.result_row = Adw.ActionRow()
        self.rows.append(self.result_row)

        # Web Row
        self.web_row = Adw.ActionRow()
        self.web_row.set_title(f"Search in web: ")
        self.web_row.set_subtitle(self.web.name)
        self.web_row.add_prefix(self.web_icon)
        self.web_row.connect("activated", self.open_in_browser)
        self.rows.append(self.web_row)

        # Result Group
        self.result_group = Adw.PreferencesGroup()
        self.result_group.set_title("Result")
        self.result_group.add(self.result_row)
        #self.result_group.set_visible(False)

        # Web Group
        self.web_group = Adw.PreferencesGroup()
        self.web_group.set_title("Web")
        self.web_group.add(self.web_row)
        self.web_button = Gtk.Button()
        self.web_button.set_label("Open in web")
        self.web_button.set_has_frame(False)
        self.web_button.connect("clicked", self.open_in_browser)
        self.web_row.add_suffix(self.web_button)

        self.page.add(self.result_group)
        self.page.add(self.web_group)

    def on_entry_changed(self, search_entry):
        self.text = search_entry.get_text()  # Remove previous search results


        if self.text:
            self.result_group.set_visible(True)
            self.set_size_request(600, 500)
            if re.match(self.calculator.pattern, self.text):
                result = self.calculator.calculate(self.text)
                self.result_row.set_title(str(result))
                self.result_row.set_subtitle(self.calculator.name)
                self.result_row.add_prefix(self.calculator_icon)

            elif re.match(self.calendar.pattern, self.text):
                result = self.calendar.get_day_of_week(re.search(self.calendar.pattern, text))
                self.result_row.set_title(result)
                self.result_row.set_subtitle(self.calendar.name)

            else:
                for result in self.files.search(self.text):
                    row = Adw.ActionRow()
                    row.set_title(result['name'])
                    row.set_subtitle(result['type'])
                    icon = Gtk.Image.new_from_icon_name(result['icon'])
                    row.add_prefix(icon)
                    row.set_can_focus(True)
                    self.result_group.add(row)
                self.result_group.set_visible(True)

            self.web_row.set_title(f"Search in web: {self.text}")
            self.web_row.set_subtitle(self.web.name)
        else:
            self.result_group.set_visible(False)
            self.set_size_request(600, -1)
            self.result_row.set_title("")
            self.result_row.set_subtitle("")
            self.web_row.set_title(f"Search in web: ")

    def remove_all_rows(self, group):
        for child in self.rows:
            group.remove(child)

    def open_in_browser(self, widget):
        text = self.search_entry.get_text()
        self.web.search(str(text))

    def open_file(self, path):
            if platform.system() == "Windows":
                # On Windows, use the 'start' command through 'cmd /c'
                subprocess.run(['cmd', '/c', 'start', '', path], shell=True)
            elif platform.system() == "Linux":
                subprocess.run(['xdg-open', path], check=True)
