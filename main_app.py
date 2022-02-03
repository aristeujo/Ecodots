import time
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import *
from appUI import UiComponents
from pages import HomePageController, FRPageController, PageConfigModel, ContactPageController, WasteDoorPageController
from pages import WasteWeighingPageController, FrErrorPageController, RewardPageController, FinalPageController
import utils

# this is the function only to make the Facial Recogntion button clickable, Nothing fancy
# call this function only if you have to make a Qlabel Clickable
# PyQT/Pyside Doesn't offer any offer any readily available method to perform an action upon click of the Qlabel
# this is why developers have to write their own functions and methods to perform the tasks


class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.appUi = UiComponents()
        self.appUi.build_ui(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def init(self):
        self.CurrentTime = '--'
        self.CurrentDate = '--'
        self.CityName = '--'
        self.CurrentTemperature = '--'

    def _RegisterPagesAndConfig(self):
        self.update_time_date()
        self.update_temperature()
        self.update_config = {
            'time': PageConfigModel('time', 60, 0, self.update_time_date),
            'temperature': PageConfigModel('time', 600, 0, self.update_temperature)
        }

        self.home_page = HomePageController(self)
        self.fr_page = FRPageController(self)
        self.contact_page = ContactPageController(self)
        self.waste_door_page = WasteDoorPageController(self)
        self.waste_weighing_page = WasteWeighingPageController(self)
        self.fr_error_page = FrErrorPageController(self)
        self.reward_page = RewardPageController(self)
        self.final_page = FinalPageController(self)

    def start(self):
        self.init()
        self._StartTimer()
        self._RegisterPagesAndConfig()
        self.home_page.start()

    def _StartTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.RunTimer)
        self.timer.start(1000)

    def set_city_name(self, city_name):
        print("----> City Name ", city_name)
        self.CityName = city_name

    def update_temperature(self):
        print('Updating Temperature')
        self.CurrentTemperature = '28'

    def update_time_date(self):
        print('Updating Clock Time')
        time_now = datetime.now()
        self.CurrentTime = time_now.strftime("%H:%M")
        self.CurrentDate = utils.get_formated_date(time_now, '%A {th}, %B')

    def RunTimer(self):

        c_time = time.time()
        for key in self.update_config:
            conf: PageConfigModel = self.update_config.get(key)
            if conf is None:
                continue

            diff = c_time - conf.LastUpdated
            if diff >= conf.Interval:
                conf.Run()
                conf.LastUpdated = c_time

        self.home_page.update_data()
        self.fr_page.update_data()
        self.fr_error_page.update_data()
        self.contact_page.update_data()
        self.waste_door_page.update_data()
        self.waste_weighing_page.update_data()
        self.reward_page.update_data()
        self.final_page.update_data()

    def recognize_face(self, image_path):
        self.home_page.on_image(image_path)

    def supportBtnClicked(self):
        print("im the support button, im clicked")

    def DialPadOKButton(self):
        print("IM the ok BUTTON from the Dial Pad of contactPage")
        self.appUi.menuNavigation.setCurrentWidget(self.appUi.wasteDoorPage)

    def yesBtnClicked(self):
        print("Yes BUTTON PRESSEEEDD")
        self.appUi.menuNavigation.setCurrentWidget(self.appUi.wasteDoorPage)

    def noBtnClicked(self):
        print("No button clicked")
        self.appUi.menuNavigation.setCurrentWidget(self.appUi.contactPage)

    def FRHomeBtnNavigation(self):
        print("Im the Facial recognition button from home Page, Im clicked")
        self.appUi.screenNavigation.setCurrentWidget(self.appUi.menuPage)
        self.appUi.menuNavigation.setCurrentWidget(self.appUi.FRPage)
