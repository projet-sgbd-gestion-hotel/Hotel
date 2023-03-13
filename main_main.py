import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

class MainMain:
    def gestionHotel(self, GestionHotel):
        #print("Hello ")
        b = gtk.Builder()
        b.add_from_file("main_main.glade")
        #window = b.get_object("fenetre_main_main")
        box = b.get_object("box_main_main")
        #print(box)
        bouton = gtk.Button(label="Description Hotel")
        box.pack_start(bouton, True, True, 0)

        box.show()

builder = gtk.Builder()

builder.add_from_file("main_main.glade")
window = builder.get_object("fenetre_main_main")

builder.connect_signals(MainMain())

window.connect("delete-event", gtk.main_quit)

window.show()

gtk.main()