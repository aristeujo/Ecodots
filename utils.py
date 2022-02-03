import datetime
from PyQt5.QtCore import *
import os, json
from collectionOperations import search_faces_with_image
from manage_camera import *

script_dir = os.path.dirname(__file__)
photo_path = os.path.join(script_dir, 'pics/temp_image.jpg')
json_path = os.path.join(script_dir, "users.json")

def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def get_formated_date(dt, f):
    day = str(dt.day) + ("th" if 4 <= dt.day % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th"))
    return dt.strftime(f).replace("{th}", day)


def get_waste_production() -> tuple:
    population = 215317263
    date_of_population = datetime.datetime.strptime("24-10-2021 17:34:34", '%d-%m-%Y %H:%M:%S')
    seconds_passed_since_data = (datetime.datetime.now() - date_of_population).total_seconds()

    seconds_from_start_of_year = (datetime.datetime.now() -
                                  datetime.datetime.strptime(f'01-01-{str(date_of_population.year)} 00:00:00',
                                                             '%d-%m-%Y %H:%M:%S')).total_seconds()

    current_population = population + seconds_passed_since_data / 16.1
    waste_produced = str(round(
        (seconds_from_start_of_year * 1.3245078e-8 * current_population) + (current_population * 1.3245078e-8))).rjust(
        8, '0')

    centenas = waste_produced[-3:]
    milhares = waste_produced[-6:-3]
    milhoes = waste_produced[:-6]

    return milhoes, milhares, centenas


def get_city_name() -> str:
    return "Manaus"


def get_temperature() -> str:
    return "30 °C"


def get_user_data_from_rekognition_api():
    # call your aws api here and replace user name from rekognition api

    takePicture()
    userFace = search_faces_with_image("Collection_ecodots", photo_path)[0]['Face']['ExternalImageId']
    with open(json_path, 'rt') as jsonFile:

        users = json.load(jsonFile)
        faceData = users[userFace]
    
    return faceData


def get_user_name_from_phone_no_api(phone_no):
    # call your aws api here and replace name from phone no api
    name = "Qaim"
    error = False
    return name, error


def get_waste_value_from_api():
    # call your sensor here
    waste_value = 1.38
    return waste_value


def get_meta_anual_data_from_api(current_value, target_value):
    # call your aws api here and replace waste_value from api
    waste_target_value = current_value
    total_target_value = target_value
    percentage = round((waste_target_value / total_target_value) * 100, 1)
    return percentage, waste_target_value, total_target_value


def get_reais_rewards(weight_kg):
    return round(weight_kg * 0.38, 2)


def get_ecodots_rewards(weight_kg):
    return round(weight_kg * 125, 2)
