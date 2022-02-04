from threading import Timer
from constants import Constants
import utils
from pages import ParentControllerClass


class WasteWeighingPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'wastePage'
        self.waste_value = 0
        self.timer = None

    def _RegisterConfigAndEvents(self):
        self.update_config = {}

        # self.AppUi.wastePage_HomeBtn.clicked.connect(self._NavigateToHomePage)
        # self.AppUi.wastePage_BackBtn.clicked.connect(self._NavigateToWasteDoorPage)

        utils.clickable(self.AppUi.wastePage).connect(self._NavigateToRewardsPage)

    def start(self):
        super().start()

        userData = self.AppUi.userData
        self.waste_value = utils.get_waste_value_from_sensor()

        self.AppUi.wastePage_WasteValue.setText(str(self.waste_value).replace('.', ','))

        percentage, waste_target_value, total_target_value = utils.get_meta_anual_data_from_api(current_value=userData['CurrentResidue'], 
                                                                                                target_value=userData['ResidueMeta'])
        self.AppUi.wastePage_wasteTargetValue.setText(str(waste_target_value))
        self.AppUi.wastePage_totalTargetValue.setText(f"/{total_target_value}")
        self.AppUi.wastePage_progressBar.setProperty("value", percentage)

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        self.timer = Timer(Constants.WasteWeighingTimer, self._NavigateToRewardsPage)
        self.timer.start()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        super().stop()

    def _NavigateToRewardsPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.rewardPage)
        self.MainApp.reward_page.set_waste_value(self.waste_value)
        self.MainApp.reward_page.start()

    def _NavigateToWasteDoorPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.wasteDoorPage)
        self.MainApp.waste_door_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()
