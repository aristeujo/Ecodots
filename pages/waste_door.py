from threading import Timer
from constants import Constants
from pages import ParentControllerClass
import utils


class WasteDoorPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'wasteDoorPage'
        self.timer = None

    def _RegisterConfigAndEvents(self):
        self.update_config = {}

        # self.AppUi.wasteDoorPageHomeBtn.clicked.connect(self._NavigateToHomePage)
        # self.AppUi.wasteDoorPageBackBtn.clicked.connect(self._NavigateToFRPage)

        utils.clickable(self.AppUi.wasteDoorPage_gifContainer).connect(self._PlayAnimation)
        self.AppUi.wasteDoorPage_gifContainer.setStyleSheet("background:none;\n"
                                                      "border-radius: 15px;\n"
                                                      "border-image: url(assets/porta.jpeg);")

    def start(self):
        super().start()
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        self.timer = Timer(Constants.WasteDoorTimer, self._PlayAnimation)
        self.timer.start()

    def stop(self):
        super().stop()
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

    def _PlayAnimation(self):
        print("Play Animation Here")
        self._NavigateToWasteWeighingPage()

    def _NavigateToWasteWeighingPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.wastePage)
        self.MainApp.waste_weighing_page.start()

    def _NavigateToFRPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FRPage)
        self.MainApp.fr_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()