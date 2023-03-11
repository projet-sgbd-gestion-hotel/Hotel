import gi

gi.require_version('Gtk','3.0')

from  gi.repository import Gtk as gtk

"""
    class qui gere les differentes actions des bouttons relatif aux fichiers main
"""
class BoutonMain:
    def gestionHotel(self, GestionHotel):
        builder = gtk.Builder()
        builder.add_from_file("hotel.glade")
        window = builder.get_object("fenetre_hotel")
        window.show()

    def quitter(self, Quitter):
        print("Au revoir, bye")
        gtk.main_quit()

class BoutonHotel:
    def descriptionHotel(self, DescriptionHotel):
        builder = gtk.Builder()
        builder.add_from_file("description.glade")
        window = builder.get_object("fenetre_description")
        window.show_all()

    def retour(self,retour):
        builder = gtk.Builder()
        builder.add_from_file("main.glade")

        window = builder.get_object("fenetre_main")
        window.show()