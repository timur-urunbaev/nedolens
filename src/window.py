# window.py
#
# Copyright 2024 Timur Urunbaev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import re
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/nedogeek/nedolens/window.ui')
class NedolensWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NedolensWindow'

    box = Gtk.Template.Child()
    search_entry = Gtk.Template.Child()
    page = Gtk.Template.Child()
    group = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_default_size(600, 70)
        # Connect to the "changed" signal of the GtkEntry
        self.search_entry.connect("changed", self.on_entry_changed)
        self.search_entry.set_size_request(600, 70)

    def on_entry_changed(self, search_entry):
        text = search_entry.get_text()

        if text:
            page_height = self.page.get_allocation().height
            print(page_height)
            self.set_size_request(600, 100+page_height)
            self.add_row(text, "integration_name")
        else:
            self.set_size_request(600, 70)

    def add_group(self):
        # Add action row dynamically
        group = Adw.PreferencesGroup()
        self.page.add(group, False, False, 0)
        group.show_all()

    def add_row(self, result, integration="?"):
        # Add action row dynamically
        action_row = Adw.ActionRow()
        self.group.add(action_row)
        action_row.set_title(result)
        action_row.set_subtitle(integration)
