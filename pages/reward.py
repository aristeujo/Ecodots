from threading import Timer
from constants import Constants
from pages import ParentControllerClass
import utils


class RewardPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'rewardPage'
        self.waste_value = 0
        self.timer = None

    def _RegisterConfigAndEvents(self):
        self.update_config = {}
        # self.AppUi.FR_errorHomeBtn.clicked.connect(lambda: self._NavigateToHomePage())
        # self.AppUi.FR_errorBackBtn.clicked.connect(lambda: self._NavigateToWasteWeighingPage())

        utils.clickable(self.AppUi.rewardPage).connect(self._NavigateToFinalPage)

    def start(self):
        super().start()
        reais_rewards = utils.get_reais_rewards(self.waste_value)
        ecodots_rewards = utils.get_ecodots_rewards(self.waste_value)

        self.AppUi.rewardPage_rewardEDAmount.setText(str(ecodots_rewards).replace('.', ','))
        self.AppUi.rewardPage_redemptionValue.setText(str(reais_rewards).replace('.', ','))

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        self.timer = Timer(Constants.RewardTimer, self._NavigateToFinalPage)
        self.timer.start()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        super().stop()

    def set_waste_value(self, waste_value):
        self.waste_value = waste_value
        print("waste_value ----> ", self.waste_value)

    def _NavigateToFinalPage(self):
        self.stop()
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.finalPage)
        self.MainApp.final_page.start()

    def _NavigateToWasteWeighingPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.wastePage)
        self.MainApp.waste_weighing_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()