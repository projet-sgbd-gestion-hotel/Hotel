import gi

gi.require_version('Gtk','3.0')

from  gi.repository import Gtk as gtk
from actions_boutons import BoutonMain, BoutonHotel


fichier_main__glade = "main.glade"
builder = gtk.Builder()
builder.add_from_file(fichier_main__glade)

builder.connect_signals(BoutonMain())
window = builder.get_object("fenetre_main")

#quitter = builder.get_object("btn_quitter")


window.connect("delete-event", gtk.main_quit)
window.show_all()

gtk.main()