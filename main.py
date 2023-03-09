import gi

gi.require_version('Gtk','3.0')

from  gi.repository import Gtk as gtk

"""
class Main:
    def __int__(self):
        fichier_glade = "fenetre1.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(fichier_glade)
        self.builder.connect_signals(self)

        window = self.builder.get_object("main")
        window.connect("delete-event",gtk.main_quit)
        window.show_all()
"""

"""
    definition des differentes methode à éffctuer sur les differents button
    
    chaque methode faire reference à un button en question  
"""

class ActionButton:
    def quitter(self, quitter):
        print("Quitter")
        gtk.main_quit()

fichier_glade = "fenetre1.glade"
builder = gtk.Builder()
builder.add_from_file(fichier_glade)

builder.connect_signals(ActionButton())

window = builder.get_object("main")
window.connect("delete-event",gtk.main_quit)
window.show_all()

gtk.main()