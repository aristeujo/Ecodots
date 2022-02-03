import sys
import geocoder

from geopy.geocoders import Nominatim
from PyQt5.QtWidgets import QApplication

from main_app import MainApp


def city_name_by_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    g = geocoder.ip('me')
    location = geolocator.reverse(str(g.latlng[0]) + "," + str(g.latlng[1]))
    return location.raw['address']['city']


def main():
    app = QApplication(sys.argv)
    win = MainApp()
    win.set_city_name('Manaus')
    win.show()
    win.start()

    # win.recognize_face("assets/face.png")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
