import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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
