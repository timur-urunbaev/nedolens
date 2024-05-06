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

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/nedogeek/nedolens/window.ui')
class NedolensWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NedolensWindow'

    entry = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Connect to the "changed" signal of the GtkEntry
        self.entry.connect("changed", self.on_entry_changed)

    def on_entry_changed(self, entry):
        text = entry.get_text()

        if text:
            self.popover.set_relative_to(self.entry)
            self.popover.show_all()
            self.popover.popup()
        else:
            self.popover.hide()
