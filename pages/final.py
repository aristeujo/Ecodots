from threading import Timer
from constants import Constants
from pages import ParentControllerClass
from pages.common import PageConfigModel
import utils


class FinalPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'finalPage'
        self.timer = None

    def _RegisterConfigAndEvents(self):
        self.update_config = {}
        # self.AppUi.finalPage_homeBtn.clicked.connect(lambda: self._NavigateToHomePage())
        # self.AppUi.finalPageBackBtn.clicked.connect(lambda: self._NavigateToRewardPage())

    def start(self):
        super().start()

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        self.timer = Timer(Constants.FinalTimer, self._NavigateToHomePage)
        self.timer.start()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        super().stop()

    def _NavigateToRewardPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.rewardPage)
        self.MainApp.reward_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()