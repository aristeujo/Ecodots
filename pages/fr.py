from datetime import datetime
import utils
import traceback

from pages import PageConfigModel, ParentControllerClass


class FRPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'menuPage'

    def _RegisterConfigAndEvents(self):
        self.update_time_date()
        self.update_city_name()
        self.update_temperature()
        self.update_config = {
            'time': PageConfigModel('time', 60, 0, self.update_time_date),
            'city_name': PageConfigModel('time', 3600, 0, self.update_city_name),
            'temperature': PageConfigModel('time', 600, 0, self.update_temperature)
        }
        # utils.clickable(self.AppUi.menu_supportBtn).connect(self._OnSupportButtonClicked)
        utils.clickable(self.AppUi.menu_noBtn).connect(self._NavigateToContactPage)
        utils.clickable(self.AppUi.menu_yesBtn).connect(self._NavigateToWasteDoorPage)

    def _NavigateToContactPage(self):
        print(f"----------{self.name} No Button Clicked ----------")
        self.stop()
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.contactPage)
        self.MainApp.contact_page.start()

    def _NavigateToWasteDoorPage(self):
        print(f"----------{self.name} Yes Button Clicked ----------")
        self.stop()
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.wasteDoorPage)
        self.MainApp.waste_door_page.start()

    def _NavigateToFrErrorPage(self):
        self.stop()
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FR_errorPage)
        self.MainApp.fr_error_page.start()

    def _OnSupportButtonClicked(self):
        print(f"----------{self.name} Support Button Clicked ----------")

    def update_city_name(self):
        city_name = utils.get_city_name()
        self.AppUi.menu_cityName.setText(city_name)

    def update_temperature(self):
        temperature = utils.get_temperature()
        self.AppUi.menu_temperature.setText(temperature)
        
    def update_time_date(self):
        print(f'{self.name} --> Updating Clock Time')
        traceback.print_exc()
        time_now = datetime.now()
        self.AppUi.menu_time.setText(time_now.strftime("%H:%M"))

    def on_image(self, image_path):
        print("on_image method in fr.py -> image_path = ", image_path)
        # self.AppUi.FR_imageContainer.setStyleSheet("background:none;\n"
        #                                            "border-radius: 15px;\n"
        #                                            f"border-image: url({image_path});")

        # * user_name, error = utils.get_user_name_from_rekognition_api(image_path)
        # * self.AppUi.FR_username.setText(user_name)

        # * if error:
        # *    self._NavigateToFrErrorPage()

