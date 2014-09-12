from gi.repository import Gtk
from grabbo import Builder

class Window(Builder, Gtk.Window):
    def __init__(self, content = Gtk.Box()):
        Gtk.Window.__init__(self)
        self.set_size_request(400, 400)
        self.connect("destroy", self.on_close)
        self.maximize()

    def on_close(self, button):
        Gtk.main_quit()