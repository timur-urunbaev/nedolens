import re
import os
import getpass

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
        self.icon = None

        self.rows = []

        # Create a Gio.Notification
        notification = Gio.Notification()

        # APP Integrations
        self.calculator = Calculator()
        self.calendar = Calendar()
        self.weather = Weather()
        self.clock = Clock()
        self.contacts = Contacts()
        self.files = Files()
        self.settings = Settings()
        self.web = Web()

        # Result Row
        self.result_row = Adw.ActionRow()
        self.result_row.add_suffix(Gtk.Image.new_from_icon_name(self.icon))
        self.rows.append(self.result_row)

        # Web Row
        self.web_row = Adw.ActionRow()
        self.web_row.set_title(f"Search in web: ")
        self.web_row.set_subtitle(self.web.name)
        self.rows.append(self.web_row)

        # Result Group
        self.result_group = Adw.PreferencesGroup()
        self.result_group.set_title("Result")
        self.result_group.add(self.result_row)

        # Web Group
        self.web_group = Adw.PreferencesGroup()
        self.web_group.set_title("Web")
        self.web_group.add(self.web_row)

        self.page.add(self.result_group)
        self.page.add(self.web_group)



    def on_entry_changed(self, search_entry):
        text = search_entry.get_text()  # Remove previous search results


        if text:
            self.result_group.set_visible(True)
            self.set_size_request(600, 500)
            if re.match(self.calculator.pattern, text):
                result = self.calculator.calculate(text)
                self.result_row.set_title(str(result))
                self.result_row.set_subtitle(self.calculator.name)
                self.result_row.connect("activated", self.copy_to_clipboard)

            elif re.match(self.calendar.pattern, text):
                result = self.calendar.get_day_of_week(re.search(self.calendar.pattern, text))
                self.result_row.set_title(result)
                self.result_row.set_subtitle(self.calendar.name)

            #elif re.match(pattern[], text):

            #elif re.match(pattern[], text):

            #elif re.match(pattern[], text):
            else:
                for result in self.files.search("/home/nedogeek/", text):
                    row = Adw.ActionRow()
                    row.set_title(result)
                    row.set_subtitle(self.files.name)
                    self.result_group.add(row)
                self.result_group.set_visible(False)

            self.web_row.set_title(f"Search in web: {text}")
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

    def show_notification(self, title, body):
        pass

    def copy_to_clipboard(self, widget, event):
        # Set notification properties
        notification.set_title("NedoLens")
        notification.set_body("Copy to clipboard")
        notification.set_urgency(Gio.NotificationUrgency.NORMAL)

        print("Copy to clipboard")
        # Show the notification
        notification.show()

    def on_key_press(self, widget, event):
        keyval = event.keyval
        if keyval == Gdk.KEY_Up:
            self.move_focus(Gtk.DirectionType.UP)
            return True
        elif keyval == Gdk.KEY_Down:
            self.move_focus(Gtk.DirectionType.DOWN)
            return True
        return False

    def move_focus(self, direction):
        current_focus = self.get_focus()
        next_focus = current_focus.get_parent().get_focus_child()
        if direction == Gtk.DirectionType.UP:
            next_focus = next_focus.get_previous_sibling()
        elif direction == Gtk.DirectionType.DOWN:
            next_focus = next_focus.get_next_sibling()
        if next_focus:
            next_focus.grab_focus()
