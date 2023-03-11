import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

class Hotel:
    def __int__(self,nom,adresse,etage = 0,chambre_par_etage = 0,chambre_total = 1):
        self.nom = nom
        self.adresse = adresse
        self.etage = etage
        self.chambre_par_etage = chambre_par_etage
        self.chambre_total = chambre_total


    def modifierNomHotel(self,new_nom):
        self.nom = new_nom

    def modifierPiece(self,etages,chambres):
        self.etage = etages
        self.chambre_total = chambres

from actions_boutons import BoutonHotel,BoutonMain


fichier_main__glade = "hotel.glade"
builder = gtk.Builder()
builder.add_from_file(fichier_main__glade)

builder.connect_signals(BoutonHotel())
window = builder.get_object("fenetre_hotel")


window.connect("delete-event", gtk.main_quit)
window.show_all()

gtk.main()