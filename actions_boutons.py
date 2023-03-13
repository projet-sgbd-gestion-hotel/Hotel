import gi

gi.require_version('Gtk', '3.0')

from  gi.repository import Gtk as gtk

"""
    class qui gere les differentes actions des bouttons relatif aux fichiers main
"""

def fonction(element1, element2):
    buider = gtk.Builder()
    buider.add_from_file(element1)
    window = buider.get_object(element2)
    window.show()

def deconnexion(fichier, element):
    builder = gtk.Builder()
    builder.add_from_file(fichier)
    elem = builder.get_object(element)
    builder.disconnect(elem)

class BoutonMain:
    def gestionHotel(self, GestionHotel):
        fonction("hotel.glade", "fenetre_hotel")
        #deconnexion("main.glade", "fenetre_main")

    def reservation(self, reservation):
        fonction("reservation.glade", "fenetre_reservation")

    def gestionClient(self, GestionClient):
        fonction("client.glade", "fenetre_client")

    def gestionChambre(self,GestionChambre):
        fonction("chambre.glade", "fenetre_chambre")

    def statistique(self, VoirStatistique):
        fonction("statistique.glade", "fenetre_statistique")

    def quitter(self, Quitter):
        print("Au revoir, bye")
        gtk.main_quit()

class BoutonHotel:
    def descriptionHotel(self, DescriptionHotel):
        fonction("description.glade", "fenetre_description")

    def retour(self, retour):
        fonction("main.glade", "fenetre_main")