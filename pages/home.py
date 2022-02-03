import utils
import random 
import os
from pages import PageConfigModel, ParentControllerClass

script_dir = os.path.dirname(os.path.dirname(__file__))
photo_path = os.path.join(script_dir, 'pics/temp_image.jpg')


class HomePageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'homePage'

    def stop(self):
        # Your Code Here
        super().stop()

    def start(self):
        super().start()
        # Your code Here

    def _RegisterConfigAndEvents(self):
        self.update_time_date()
        self.update_city_name()
        self.update_temperature()
        self.update_config = {
            'time': PageConfigModel('time', 60, 0, self.update_time_date),
            'city_name': PageConfigModel('time', 3600, 0, self.update_city_name),
            'temperature': PageConfigModel('time', 600, 0, self.update_temperature),
            'waste_counter': PageConfigModel('time', 17, 0, self.update_waste_production_counter)
        }

        # Comment Following Click Event
        utils.clickable(self.AppUi.homePage_FRButton).connect(self._OnFaceRecogButtonClicked)

    # def _OnFaceRecogButtonClicked(self):
    #     self.stop()
    #     self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.menuPage)
    #     self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FRPage)
    #     self.MainApp.fr_page.start()

    def _OnFaceRecogButtonClicked(self):
        self.stop()
        
        try:
            self.AppUi.userData = utils.get_user_data_from_rekognition_api()
            userData = self.AppUi.userData
            print(userData)
            name = userData['Name'].split(' ', 1)[0]

            print("photo path is", photo_path)

            self.AppUi.FR_imageContainer.setStyleSheet("background:none;\n"
                                "border-radius: 15px;\n"
                                "border-image: url({});".format(photo_path))
            
            utils.deletePicture()

            self.AppUi.FR_username.setText(name + "?")
            self.AppUi.weighing_username.setText(name + ",")
            self.AppUi.rewardPage_username.setText(name + ",")
            self.AppUi.wasteDoorPage_Username.setText(name + ",")
            self.AppUi.finalPage_username.setText(name + ",")
            
            self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.menuPage)
            self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FRPage)
            self.MainApp.fr_page.start()

        except Exception as e:
            print("An error has occurred:", e)
            # self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.FR_errorPage)
            # self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FR_errorPage)
            # self.MainApp.fr_error_page.start()

    def update_city_name(self):
        city_name = utils.get_city_name()
        self.AppUi.homePage_cityName.setText(city_name)

    def update_temperature(self):
        temperature = utils.get_temperature()
        self.AppUi.homePage_temperature.setText(temperature)

    def update_time_date(self):
        self.AppUi.homePage_time.setText(self.MainApp.CurrentTime)
        self.AppUi.homePage_date.setText(self.MainApp.CurrentDate)

    def update_waste_production_counter(self, waste_production: tuple = None) -> None:
        print(f"{self.name} --> Updating Waste Production Counter ")
        if waste_production is None:
            waste_production = utils.get_waste_production()

        milhoes, mihares, centenas = waste_production

        self.AppUi.homePage_counterMilhoes.setText(milhoes)
        self.AppUi.homePage_counterMihares.setText(mihares)
        self.AppUi.homePage_counterCentenas.setText(centenas)

    def on_image(self, image_path):
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.menuPage)
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FRPage)
        self.MainApp.fr_page.on_image(image_path)

