
from gi.repository import Gtk
import grabbo

TBui = grabbo.ui.TAB_UI  #os.path.join('..', 'ui', 'TabButton.ui')
gtknever = Gtk.PolicyType.NEVER
gtknone = Gtk.ShadowType.NONE
gtkright = Gtk.DirectionType.RIGHT

class TabButton(grabbo.Builder):
    def __init__(self):
        super(TabButton, self).__init__(TBui)
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("Close")

        self.close.connect("clicked", lambda x: self.on_close())
        self.button.connect("clicked", lambda x: self.on_button())

    def set(self, notebook, num, label, closeable = True):
        self.set_closeable(closeable)
        self.button.set_label(label)
        self.notebook = notebook
        self.num = num

    def get(self):
        return self.ui.get_object("box")

    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self):
        self.notebook.pages.set_current_page(self.num)

    def on_close(self):
        self.notebook.pages.prev_page()
        self.notebook.pages.remove_page(self.num)
        self.notebook.buttons_box.remove(self.get())


class Notebook(Gtk.Box): #os.path.join("..", "ui", "notebook.ui")
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__()
        self.props.hexpand = True
        self.props.vexpand = False

        self._scrolledwindow = Gtk.ScrolledWindow()
        self._scrolledwindow.props.hexpand = True
        self._scrolledwindow.props.vexpand = False
        self._scrolledwindow.props.vscrollbar_policy = gtknever

        self._viewport = Gtk.Viewport()
        self._viewport.props.visible = True
        self._viewport.props.can_focus = False
        self._viewport.props.hexpand = True
        self._viewport.props.vexpand = False
        self._viewport.props.shadow_type = gtknone

        self.ButtonBox = Gtk.Box()
        self.ButtonBox.props.visible = True
        self.ButtonBox.props.can_focus = False
        self.ButtonBox.props.hexpand = True
        self.ButtonBox.props.vexpand = False

        #<property name="expand">True</property>
        #<property name="fill">True</property>

        AddIcon = Gtk.Image()
        AddIcon.new_from_icon_name("list-add", 4)

        self.Add = Gtk.Button()
        self.Add.props.visible = True
        self.Add.props.can_focus = True
        self.Add.props.receives_default = True
        self.Add.props.image = AddIcon
        self.Add.props.relief = gtknone
        self.Add.props.image_position = gtkright

        #<property name="expand">False</property>
        #<property name="fill">False</property>
        #<property name="position">1</property>

        self.pack_end(self.Add, True, True, True)
        self._scrolledwindow.add(self._viewport)
        self._viewport.add()
        self.pack_start(self._scrolledwindow, True, True, True)
        self.show_all()

        self.stack = Gtk.Stack()
        self.set_addable(addable)
        self.set_orientation(orientation)
        self.Add.connect("clicked", lambda x: self.add_tab())
        self.show_all()

    def add_tab(self, content, bt = TabButton(), closeable = True):
        self.pages.append_page(content)
        n = self.pages.page_num(content)

        bt.notebook = self
        bt.num = n
        bt.set_closeable(closeable)
        content.show()

        self.ButtonBox.add(bt.get())

    def set_addable(self, addable):
        if not addable:
            self.Add.hide()

